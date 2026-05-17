# Billing Service
# Handles insurance claims and payment processing
# WARNING: Contains intentional PHI violations for demo purposes

from flask import Flask, request, jsonify
import requests
import logging
import json
import config

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation #6: HTTP not HTTPS for patient API calls
# HIPAA Rule: §164.312(e)(1) - Transmission security
PATIENT_API_URL = "http://localhost:5001"  # Should use HTTPS

# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation #7: Caching PHI in plaintext file
# HIPAA Rule: §164.312(a)(1) - Access control - encryption at rest
CLAIMS_CACHE_FILE = "claims_cache.json"

def load_claims():
    try:
        with open(CLAIMS_CACHE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_claims(claims):
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #7 continued: Writing PHI to unencrypted file
    with open(CLAIMS_CACHE_FILE, "w") as f:
        json.dump(claims, f, indent=2)

# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation #10: No rate limiting on claim submission
# HIPAA Rule: §164.308(a)(1)(ii)(D) - Information system activity review
# Reference: See config.py - RATE_LIMIT_ENABLED = False
@app.route("/claims", methods=["POST"])
def submit_claim():
    data = request.json
    patient_id = data["patient_id"]

    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #6 continued: Fetching PHI over HTTP
    response = requests.get(f"{PATIENT_API_URL}/patients/{patient_id}")
    patient = response.json()

    claim = {
        "claim_id": f"CLM-{len(load_claims()) + 1:04d}",
        "patient_name": patient["full_name"],
        # INTENTIONAL HIPAA VIOLATION FOR DEMO
        # Violation #8: Storing SSN in claim (minimum necessary principle)
        # HIPAA Rule: §164.502(b) - Minimum necessary
        "patient_ssn": patient["ssn"],
        "patient_dob": patient["date_of_birth"],
        "diagnosis_code": data["diagnosis_code"],
        "procedure_code": data["procedure_code"],
        "amount": data["amount"],
        "insurance_id": data["insurance_id"],
        "status": "submitted"
    }

    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #9: Logging full claim with PHI
    # HIPAA Rule: §164.312(b) - Audit controls
    logger.debug(f"Submitting claim: {json.dumps(claim)}")

    claims = load_claims()
    claims.append(claim)
    save_claims(claims)

    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation: Returning PHI in response without access control
    return jsonify(claim), 201

@app.route("/claims/<claim_id>", methods=["GET"])
def get_claim(claim_id):
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation: No authentication required
    # HIPAA Rule: §164.312(d) - Person or entity authentication
    claims = load_claims()
    for claim in claims:
        if claim["claim_id"] == claim_id:
            # INTENTIONAL HIPAA VIOLATION FOR DEMO
            # Violation #9 continued: Logging PHI on every access
            logger.info(f"Claim accessed: {claim['patient_name']} SSN:{claim['patient_ssn']}")
            return jsonify(claim)
    return jsonify({"error": "Claim not found"}), 404

@app.route("/claims/patient/<int:patient_id>", methods=["GET"])
def get_patient_claims(patient_id):
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation: No role-based access control
    # HIPAA Rule: §164.308(a)(4) - Information access management
    response = requests.get(f"{PATIENT_API_URL}/patients/{patient_id}")
    patient = response.json()
    claims = load_claims()
    patient_claims = [c for c in claims if c["patient_ssn"] == patient["ssn"]]
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #9 continued: Logging patient lookup with SSN
    logger.info(f"Claims lookup for SSN: {patient['ssn']} found {len(patient_claims)} claims")
    return jsonify(patient_claims)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
