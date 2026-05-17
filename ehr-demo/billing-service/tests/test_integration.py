# Billing Service Integration Tests
# Tests cross-service PHI flow and cache violations

import pytest
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, CLAIMS_CACHE_FILE

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    if os.path.exists(CLAIMS_CACHE_FILE):
        os.remove(CLAIMS_CACHE_FILE)
    with app.test_client() as client:
        yield client
    if os.path.exists(CLAIMS_CACHE_FILE):
        os.remove(CLAIMS_CACHE_FILE)

def test_phi_propagates_across_services(client, monkeypatch):
    """
    VIOLATION TEST: Verify PHI flows from patient-api to billing-service unencrypted
    """
    # Mock patient API to return PHI
    class MockResponse:
        def json(self):
            return {
                "id": 1,
                "full_name": "Cross Service Test",
                "ssn": "888-99-0000",
                "date_of_birth": "1975-06-20",
                "medical_record_number": "MRN-CROSS",
                "diagnosis": "Test Condition"
            }
    
    import requests
    monkeypatch.setattr(requests, "get", lambda url: MockResponse())
    
    claim_data = {
        "patient_id": 1,
        "diagnosis_code": "E11.9",
        "procedure_code": "99213",
        "amount": 200.00,
        "insurance_id": "INS-CROSS"
    }
    
    response = client.post('/claims', json=claim_data)
    assert response.status_code == 201
    
    claim = response.get_json()
    
    # VIOLATION: PHI propagated from patient-api to billing-service
    assert claim['patient_ssn'] == "888-99-0000"
    assert claim['patient_name'] == "Cross Service Test"

def test_cache_file_contains_plaintext_phi(client, monkeypatch):
    """
    VIOLATION TEST: Verify cache file stores PHI in plaintext JSON
    """
    class MockResponse:
        def json(self):
            return {
                "id": 1,
                "full_name": "Cache Test Patient",
                "ssn": "777-88-9999",
                "date_of_birth": "1988-08-08",
                "medical_record_number": "MRN-CACHE"
            }
    
    import requests
    monkeypatch.setattr(requests, "get", lambda url: MockResponse())
    
    claim_data = {
        "patient_id": 1,
        "diagnosis_code": "I10",
        "procedure_code": "99214",
        "amount": 175.00,
        "insurance_id": "INS-CACHE"
    }
    
    response = client.post('/claims', json=claim_data)
    assert response.status_code == 201
    
    # VIOLATION: Read cache file directly
    assert os.path.exists(CLAIMS_CACHE_FILE)
    with open(CLAIMS_CACHE_FILE, 'r') as f:
        content = f.read()
    
    # VIOLATION: PHI is readable in plaintext
    assert "777-88-9999" in content, "SSN should be encrypted but is plaintext in cache"
    assert "Cache Test Patient" in content, "Name should be encrypted but is plaintext"

def test_phi_logged_during_claim_processing(client, monkeypatch, caplog):
    """
    VIOLATION TEST: Verify PHI is logged during claim submission
    """
    import logging
    caplog.set_level(logging.DEBUG)
    
    class MockResponse:
        def json(self):
            return {
                "id": 1,
                "full_name": "Log Test",
                "ssn": "666-77-8888",
                "date_of_birth": "1992-03-10",
                "medical_record_number": "MRN-LOG"
            }
    
    import requests
    monkeypatch.setattr(requests, "get", lambda url: MockResponse())
    
    claim_data = {
        "patient_id": 1,
        "diagnosis_code": "J45.9",
        "procedure_code": "99215",
        "amount": 225.00,
        "insurance_id": "INS-LOG"
    }
    
    response = client.post('/claims', json=claim_data)
    assert response.status_code == 201
    
    # VIOLATION: Check if PHI appears in logs
    log_output = caplog.text
    assert "666-77-8888" in log_output or "Log Test" in log_output, "PHI should not be in logs"

# MISSING INTEGRATION TESTS (commented to show what SHOULD exist):

# def test_tls_enforced_for_cross_service_calls(client):
#     """This test would FAIL - HTTP used instead of HTTPS"""
#     # Should verify all service-to-service calls use TLS 1.2+
#     pass

# def test_cache_encryption_at_rest(client):
#     """This test would FAIL - cache is plaintext"""
#     # Should verify cache file is encrypted
#     pass

# def test_audit_trail_for_phi_access(client):
#     """This test would FAIL - no audit logging"""
#     # Should verify audit log entry for each PHI access
#     pass

# Made with Bob
