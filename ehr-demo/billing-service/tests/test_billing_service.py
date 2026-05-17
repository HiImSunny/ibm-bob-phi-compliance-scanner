# Billing Service Unit Tests
# These tests PASS because they verify the violations exist (for demo purposes)

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
    # Clean up cache file before each test
    if os.path.exists(CLAIMS_CACHE_FILE):
        os.remove(CLAIMS_CACHE_FILE)
    with app.test_client() as client:
        yield client
    # Clean up after test
    if os.path.exists(CLAIMS_CACHE_FILE):
        os.remove(CLAIMS_CACHE_FILE)

def test_submit_claim_uses_http_not_https(client, monkeypatch):
    """
    VIOLATION TEST: Verify service calls patient API over HTTP
    """
    # Mock the patient API response
    class MockResponse:
        def json(self):
            return {
                "id": 1,
                "full_name": "Test Patient",
                "ssn": "123-45-6789",
                "date_of_birth": "1985-03-15",
                "medical_record_number": "MRN-001234"
            }
    
    def mock_get(url):
        # VIOLATION: Verify URL uses HTTP not HTTPS
        assert url.startswith("http://"), "Should use HTTPS but uses HTTP"
        return MockResponse()
    
    import requests
    monkeypatch.setattr(requests, "get", mock_get)
    
    claim_data = {
        "patient_id": 1,
        "diagnosis_code": "E11.9",
        "procedure_code": "99213",
        "amount": 150.00,
        "insurance_id": "INS-12345"
    }
    
    response = client.post('/claims', json=claim_data)
    assert response.status_code == 201

def test_claim_stores_ssn_in_cache(client, monkeypatch):
    """
    VIOLATION TEST: Verify SSN is stored in plaintext cache file
    """
    # Mock patient API
    class MockResponse:
        def json(self):
            return {
                "id": 1,
                "full_name": "Test Patient",
                "ssn": "999-88-7777",
                "date_of_birth": "1990-01-01",
                "medical_record_number": "MRN-TEST"
            }
    
    import requests
    monkeypatch.setattr(requests, "get", lambda url: MockResponse())
    
    claim_data = {
        "patient_id": 1,
        "diagnosis_code": "E11.9",
        "procedure_code": "99213",
        "amount": 150.00,
        "insurance_id": "INS-12345"
    }
    
    response = client.post('/claims', json=claim_data)
    assert response.status_code == 201
    
    # VIOLATION: Verify SSN is in plaintext cache file
    assert os.path.exists(CLAIMS_CACHE_FILE)
    with open(CLAIMS_CACHE_FILE, 'r') as f:
        cache_data = json.load(f)
    
    assert len(cache_data) > 0
    claim = cache_data[0]
    assert 'patient_ssn' in claim
    assert claim['patient_ssn'] == "999-88-7777", "SSN should be encrypted but is plaintext"

def test_no_rate_limiting_on_claims(client, monkeypatch):
    """
    VIOLATION TEST: Verify no rate limiting allows bulk submissions
    """
    # Mock patient API
    class MockResponse:
        def json(self):
            return {
                "id": 1,
                "full_name": "Test Patient",
                "ssn": "111-22-3333",
                "date_of_birth": "1985-05-15",
                "medical_record_number": "MRN-001"
            }
    
    import requests
    monkeypatch.setattr(requests, "get", lambda url: MockResponse())
    
    claim_data = {
        "patient_id": 1,
        "diagnosis_code": "E11.9",
        "procedure_code": "99213",
        "amount": 150.00,
        "insurance_id": "INS-12345"
    }
    
    # VIOLATION: Submit many claims rapidly without rate limiting
    for i in range(20):
        response = client.post('/claims', json=claim_data)
        assert response.status_code == 201, f"Request {i} should succeed (no rate limit)"

def test_get_claim_returns_phi_without_auth(client, monkeypatch):
    """
    VIOLATION TEST: Verify claim endpoint returns PHI without authentication
    """
    # First create a claim
    class MockResponse:
        def json(self):
            return {
                "id": 1,
                "full_name": "Test Patient",
                "ssn": "555-66-7777",
                "date_of_birth": "1980-12-25",
                "medical_record_number": "MRN-XYZ"
            }
    
    import requests
    monkeypatch.setattr(requests, "get", lambda url: MockResponse())
    
    claim_data = {
        "patient_id": 1,
        "diagnosis_code": "E11.9",
        "procedure_code": "99213",
        "amount": 150.00,
        "insurance_id": "INS-12345"
    }
    
    create_response = client.post('/claims', json=claim_data)
    claim_id = create_response.get_json()['claim_id']
    
    # VIOLATION: Get claim without authentication
    response = client.get(f'/claims/{claim_id}')
    assert response.status_code == 200
    
    data = response.get_json()
    # VIOLATION: PHI is exposed
    assert 'patient_ssn' in data
    assert 'patient_name' in data

# MISSING TESTS (commented to show what SHOULD exist):

# def test_rate_limiting_enforced(client):
#     """This test would FAIL - no rate limiting implemented"""
#     # Should reject requests after limit exceeded
#     pass

# def test_phi_encrypted_in_cache(client):
#     """This test would FAIL - cache stores plaintext PHI"""
#     # Should verify cache file contains encrypted data
#     pass

# def test_https_required_for_api_calls(client):
#     """This test would FAIL - uses HTTP not HTTPS"""
#     # Should verify all external calls use HTTPS
#     pass

# def test_authentication_required(client):
#     """This test would FAIL - no auth on endpoints"""
#     response = client.get('/claims/CLM-0001')
#     assert response.status_code == 401

# Made with Bob
