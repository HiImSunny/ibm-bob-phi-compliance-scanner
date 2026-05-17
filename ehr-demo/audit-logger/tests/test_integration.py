# Audit Logger Integration Tests
# Tests log file violations and retention policy issues

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, LOG_FILE, audit_events

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    audit_events.clear()
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    with app.test_client() as client:
        yield client
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

def test_phi_written_to_plaintext_log_file(client):
    """
    VIOLATION TEST: Verify PHI is written to unencrypted log file
    """
    event_data = {
        "event_type": "patient_access",
        "user_id": "user123",
        "patient_name": "File Test Patient",
        "patient_ssn": "777-88-9999",
        "patient_mrn": "MRN-FILE",
        "action": "view_record",
        "details": "Test log file violation"
    }
    
    response = client.post('/log', json=event_data)
    assert response.status_code == 201
    
    # VIOLATION: Check log file contains plaintext PHI
    assert os.path.exists(LOG_FILE)
    
    with open(LOG_FILE, 'r') as f:
        log_content = f.read()
    
    # VIOLATION: PHI is readable in plaintext
    assert "777-88-9999" in log_content, "SSN should be redacted but is in plaintext log"
    assert "File Test Patient" in log_content, "Name should be masked but is in plaintext log"

def test_no_log_retention_policy(client):
    """
    VIOLATION TEST: Verify logs are stored indefinitely without cleanup
    """
    # Create multiple audit events
    for i in range(10):
        event_data = {
            "event_type": "patient_access",
            "user_id": f"user{i}",
            "patient_name": f"Patient {i}",
            "patient_ssn": f"{i}{i}{i}-{i}{i}-{i}{i}{i}{i}",
            "patient_mrn": f"MRN-{i:03d}",
            "action": "view",
            "details": "test"
        }
        client.post('/log', json=event_data)
    
    # VIOLATION: All events remain in memory (no retention limit)
    assert len(audit_events) == 10, "Should have retention policy but stores all events"
    
    # VIOLATION: Log file grows unbounded
    assert os.path.exists(LOG_FILE)
    file_size = os.path.getsize(LOG_FILE)
    assert file_size > 0, "Log file should have size limits but doesn't"

def test_ip_address_stored_as_phi(client):
    """
    VIOLATION TEST: Verify IP addresses are stored (PHI under HIPAA)
    """
    event_data = {
        "event_type": "patient_access",
        "user_id": "user123",
        "patient_name": "IP Test",
        "patient_ssn": "888-99-0000",
        "patient_mrn": "MRN-IP",
        "action": "view",
        "details": "test"
    }
    
    response = client.post('/log', json=event_data)
    assert response.status_code == 201
    
    # VIOLATION: IP address is stored (PHI identifier)
    event = audit_events[0]
    assert 'ip_address' in event, "IP address is stored (HIPAA identifier)"
    assert event['ip_address'] is not None

def test_no_log_access_auditing(client):
    """
    VIOLATION TEST: Verify accessing logs doesn't create audit trail
    """
    # Create initial event
    event_data = {
        "event_type": "patient_access",
        "user_id": "user123",
        "patient_name": "Audit Trail Test",
        "patient_ssn": "666-77-8888",
        "patient_mrn": "MRN-TRAIL",
        "action": "view",
        "details": "test"
    }
    client.post('/log', json=event_data)
    
    initial_count = len(audit_events)
    
    # Access logs multiple times
    client.get('/logs')
    client.get('/logs/patient/666-77-8888')
    client.get('/logs/export')
    
    # VIOLATION: No audit events created for log access
    assert len(audit_events) == initial_count, "Should audit log access but doesn't"

# MISSING INTEGRATION TESTS (commented to show what SHOULD exist):

# def test_log_file_encryption(client):
#     """This test would FAIL - log file is plaintext"""
#     # Should verify log file is encrypted at rest
#     pass

# def test_log_rotation_policy(client):
#     """This test would FAIL - no log rotation"""
#     # Should verify logs are rotated after size/time limit
#     pass

# def test_log_archival_after_retention_period(client):
#     """This test would FAIL - no archival"""
#     # Should verify old logs are archived per HIPAA 6-year requirement
#     pass

# def test_audit_log_integrity_verification(client):
#     """This test would FAIL - no integrity checks"""
#     # Should verify logs have checksums/signatures to prevent tampering
#     pass

# Made with Bob
