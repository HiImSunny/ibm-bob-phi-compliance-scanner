# Patient API Integration Tests
# Tests that verify violations in database and logging behavior

import pytest
import sys
import os
import sqlite3
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, init_db, get_db

@pytest.fixture
def client():
    """Create test client with real database"""
    app.config['TESTING'] = True
    init_db()
    with app.test_client() as client:
        yield client

def test_phi_stored_in_plaintext_database(client):
    """
    VIOLATION TEST: Verify PHI is stored unencrypted in SQLite
    """
    # Create a patient
    new_patient = {
        "full_name": "Integration Test",
        "ssn": "111-22-3333",
        "date_of_birth": "1985-05-15",
        "medical_record_number": "MRN-INT001",
        "diagnosis": "Test Diagnosis",
        "phone_number": "555-0100",
        "email": "integration@test.com",
        "address": "456 Test Ave"
    }
    
    response = client.post('/patients', json=new_patient)
    assert response.status_code == 201
    
    # VIOLATION: Query database directly to verify plaintext storage
    db = get_db()
    cursor = db.execute("SELECT ssn, full_name FROM patients WHERE ssn = ?", ("111-22-3333",))
    row = cursor.fetchone()
    
    # VIOLATION: SSN is stored in plaintext
    assert row is not None
    assert row['ssn'] == "111-22-3333", "SSN should be encrypted but is plaintext"
    assert row['full_name'] == "Integration Test", "Name should be encrypted but is plaintext"

def test_phi_logged_to_console(client, caplog):
    """
    VIOLATION TEST: Verify PHI is logged to console/logs
    """
    import logging
    caplog.set_level(logging.INFO)
    
    # Access patient endpoint
    response = client.get('/patients/1')
    
    # VIOLATION: Check if PHI appears in logs
    log_output = caplog.text
    
    # The app logs patient data, which is a violation
    assert 'SSN' in log_output or 'patient' in log_output.lower()

# MISSING INTEGRATION TESTS (commented to show what SHOULD exist):

# def test_phi_encrypted_at_rest(client):
#     """This test would FAIL - PHI should be encrypted in database"""
#     db = get_db()
#     cursor = db.execute("SELECT ssn FROM patients WHERE id = 1")
#     row = cursor.fetchone()
#     # Should verify SSN is encrypted (not readable plaintext)
#     assert not row['ssn'].startswith('123-'), "SSN should be encrypted"

# def test_audit_trail_for_database_access(client):
#     """This test would FAIL - no audit trail for DB queries"""
#     # Should verify audit log entry created for each DB access
#     pass

# def test_tls_required_for_connections(client):
#     """This test would FAIL - app runs on HTTP not HTTPS"""
#     # Should verify TLS 1.2+ is enforced
#     pass

# Made with Bob
