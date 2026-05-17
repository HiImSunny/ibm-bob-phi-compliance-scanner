# Audit Logger Unit Tests
# These tests PASS because they verify the violations exist (for demo purposes)

import pytest
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, LOG_FILE, audit_events

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    # Clear in-memory audit events
    audit_events.clear()
    # Clean up log file
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    with app.test_client() as client:
        yield client
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

def test_log_event_accepts_phi(client):
    """
    VIOLATION TEST: Verify log endpoint accepts and stores raw PHI
    """
    event_data = {
        "event_type": "patient_access",
        "user_id": "user123",
        "patient_name": "Test Patient",
        "patient_ssn": "123-45-6789",
        "patient_mrn": "MRN-001234",
        "action": "view_record",
        "details": "Accessed patient record"
    }
    
    response = client.post('/log', json=event_data)
    assert response.status_code == 201
    
    # VIOLATION: PHI is stored in memory
    assert len(audit_events) == 1
    event = audit_events[0]
    assert event['patient_ssn'] == "123-45-6789", "SSN should be redacted but isn't"
    assert event['patient_name'] == "Test Patient", "Name should be masked but isn't"

def test_get_logs_returns_all_phi_without_auth(client):
    """
    VIOLATION TEST: Verify /logs endpoint returns all PHI without authentication
    """
    # Create some audit events with PHI
    events = [
        {
            "event_type": "patient_access",
            "user_id": "user1",
            "patient_name": "Patient One",
            "patient_ssn": "111-11-1111",
            "patient_mrn": "MRN-001",
            "action": "view",
            "details": "test"
        },
        {
            "event_type": "patient_update",
            "user_id": "user2",
            "patient_name": "Patient Two",
            "patient_ssn": "222-22-2222",
            "patient_mrn": "MRN-002",
            "action": "update",
            "details": "test"
        }
    ]
    
    for event in events:
        client.post('/log', json=event)
    
    # VIOLATION: Get all logs without authentication
    response = client.get('/logs')
    assert response.status_code == 200
    
    data = response.get_json()
    assert len(data) == 2
    
    # VIOLATION: All PHI is exposed
    assert data[0]['patient_ssn'] == "111-11-1111"
    assert data[1]['patient_ssn'] == "222-22-2222"

def test_ssn_used_as_url_parameter(client):
    """
    VIOLATION TEST: Verify SSN is used in URL path (exposed in server logs)
    """
    # Create an audit event
    event_data = {
        "event_type": "patient_access",
        "user_id": "user123",
        "patient_name": "URL Test",
        "patient_ssn": "999-88-7777",
        "patient_mrn": "MRN-URL",
        "action": "view",
        "details": "test"
    }
    client.post('/log', json=event_data)
    
    # VIOLATION: SSN in URL path
    response = client.get('/logs/patient/999-88-7777')
    assert response.status_code == 200
    
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['patient_ssn'] == "999-88-7777"

def test_export_creates_unencrypted_file(client):
    """
    VIOLATION TEST: Verify export creates plaintext file with PHI
    """
    # Create audit events
    event_data = {
        "event_type": "patient_access",
        "user_id": "user123",
        "patient_name": "Export Test",
        "patient_ssn": "555-66-7777",
        "patient_mrn": "MRN-EXPORT",
        "action": "view",
        "details": "test"
    }
    client.post('/log', json=event_data)
    
    # VIOLATION: Export without authentication or encryption
    response = client.get('/logs/export')
    assert response.status_code == 200
    
    # VIOLATION: Check export file exists and contains plaintext PHI
    export_file = "audit_export.json"
    assert os.path.exists(export_file)
    
    with open(export_file, 'r') as f:
        export_data = json.load(f)
    
    assert export_data['total_events'] == 1
    assert export_data['events'][0]['patient_ssn'] == "555-66-7777"
    
    # Clean up
    os.remove(export_file)

def test_no_access_control_on_export(client):
    """
    VIOLATION TEST: Verify export endpoint has no authentication
    """
    # VIOLATION: Export without any credentials
    response = client.get('/logs/export')
    
    # Should return 401, but returns 200 (violation)
    assert response.status_code == 200, "Export should require auth but doesn't"

def test_no_audit_trail_for_log_access(client):
    """
    VIOLATION TEST: Verify no audit trail when accessing audit logs
    """
    # Create an event
    event_data = {
        "event_type": "patient_access",
        "user_id": "user123",
        "patient_name": "Audit Test",
        "patient_ssn": "444-55-6666",
        "patient_mrn": "MRN-AUDIT",
        "action": "view",
        "details": "test"
    }
    client.post('/log', json=event_data)
    
    initial_count = len(audit_events)
    
    # Access the logs
    client.get('/logs')
    
    # VIOLATION: No new audit event created for accessing audit logs
    assert len(audit_events) == initial_count, "Should audit log access but doesn't"

# MISSING TESTS (commented to show what SHOULD exist):

# def test_phi_encrypted_in_logs(client):
#     """This test would FAIL - PHI is stored in plaintext"""
#     # Should verify PHI is encrypted or tokenized in audit logs
#     pass

# def test_authentication_required_for_logs(client):
#     """This test would FAIL - no auth on /logs endpoint"""
#     response = client.get('/logs')
#     assert response.status_code == 401

# def test_log_retention_policy_enforced(client):
#     """This test would FAIL - no retention policy"""
#     # Should verify old logs are archived/deleted per policy
#     pass

# def test_audit_log_access_is_audited(client):
#     """This test would FAIL - no meta-auditing"""
#     # Should verify accessing audit logs creates audit entry
#     pass

# def test_export_requires_encryption(client):
#     """This test would FAIL - export is plaintext"""
#     # Should verify export file is encrypted
#     pass

# Made with Bob
