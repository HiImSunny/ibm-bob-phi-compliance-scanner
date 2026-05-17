# Patient API Unit Tests
# These tests PASS because they verify the violations exist (for demo purposes)

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, init_db

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    app.config['DATABASE'] = ':memory:'  # Use in-memory DB for tests
    init_db()
    with app.test_client() as client:
        yield client

def test_list_patients_returns_phi(client):
    """
    VIOLATION TEST: Verify that raw PHI is exposed in API response
    This test PASSES, proving the violation exists
    """
    response = client.get('/patients')
    data = response.get_json()
    
    assert response.status_code == 200
    assert len(data) > 0
    
    # VIOLATION: These fields should NOT be in the response without encryption
    patient = data[0]
    assert 'ssn' in patient, "SSN should be redacted but isn't"
    assert 'date_of_birth' in patient, "DOB should be redacted but isn't"
    assert 'full_name' in patient, "Full name should be masked but isn't"
    
    # Verify it's actual PHI, not masked
    assert '-' in patient['ssn'], "SSN is in plaintext format"

def test_no_authentication_required(client):
    """
    VIOLATION TEST: Verify endpoint has no authentication
    This test PASSES because there's no auth - that's the violation
    """
    # No Authorization header provided
    response = client.get('/patients')
    
    # VIOLATION: Should return 401 Unauthorized, but returns 200
    assert response.status_code == 200, "Endpoint should require auth but doesn't"

def test_get_patient_by_id_exposes_phi(client):
    """
    VIOLATION TEST: Verify individual patient endpoint exposes PHI
    """
    response = client.get('/patients/1')
    
    if response.status_code == 200:
        data = response.get_json()
        
        # VIOLATION: All PHI fields are exposed
        assert 'ssn' in data
        assert 'medical_record_number' in data
        assert 'diagnosis' in data
        assert 'address' in data

def test_create_patient_accepts_plaintext_phi(client):
    """
    VIOLATION TEST: Verify POST endpoint accepts and stores plaintext PHI
    """
    new_patient = {
        "full_name": "Test Patient",
        "ssn": "999-88-7777",
        "date_of_birth": "1990-01-01",
        "medical_record_number": "MRN-TEST001",
        "diagnosis": "Test Condition",
        "phone_number": "555-0199",
        "email": "test@example.com",
        "address": "123 Test St"
    }
    
    response = client.post('/patients', json=new_patient)
    
    # VIOLATION: Accepts plaintext PHI without encryption
    assert response.status_code == 201
    data = response.get_json()
    
    # VIOLATION: Returns SSN in response
    assert 'ssn' in data

# MISSING TESTS (commented to show what SHOULD exist but doesn't):

# def test_authentication_required(client):
#     """This test would FAIL because auth is not implemented"""
#     response = client.get('/patients')  # No auth header
#     assert response.status_code == 401, "Should require authentication"

# def test_phi_is_encrypted_in_response(client):
#     """This test would FAIL because PHI is not encrypted"""
#     response = client.get('/patients/1')
#     data = response.get_json()
#     assert 'ssn' not in data or data['ssn'].startswith('***'), "SSN should be masked"

# def test_audit_log_created_on_access(client):
#     """This test would FAIL because audit logging is not implemented"""
#     response = client.get('/patients/1')
#     # Should verify audit log entry was created
#     pass

# def test_role_based_access_control(client):
#     """This test would FAIL because RBAC is not implemented"""
#     # Only clinicians should access patient records
#     pass

# Made with Bob
