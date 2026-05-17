# Patient API Service
# This service handles patient CRUD operations
# WARNING: Contains intentional PHI violations for demo purposes

from flask import Flask, request, jsonify
import sqlite3
import logging
import config

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation #5: Hardcoded encryption key in config
# Reference: See config.py - ENCRYPTION_KEY is hardcoded in source code
# HIPAA Rule: §164.312(a)(2)(iv) - Encryption and decryption key management
ENCRYPTION_KEY = config.ENCRYPTION_KEY  # This key is exposed in source control

# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation #1: Database stores PHI in plaintext
# HIPAA Rule: §164.312(a)(1) - Access control - encryption at rest
def get_db():
    conn = sqlite3.connect("patients.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            full_name TEXT,
            ssn TEXT,
            date_of_birth TEXT,
            medical_record_number TEXT,
            diagnosis TEXT,
            phone_number TEXT,
            email TEXT,
            address TEXT
        )
    """)
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #1 continued: Seed data with raw PHI in plaintext
    db.execute("""
        INSERT OR IGNORE INTO patients (id, full_name, ssn, date_of_birth, medical_record_number, diagnosis, phone_number, email, address)
        VALUES (1, 'John Smith', '123-45-6789', '1985-03-15', 'MRN-001234', 'Type 2 Diabetes', '555-0123', 'john.smith@email.com', '123 Main St, Boston, MA 02101')
    """)
    db.commit()

# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation #4: No authentication/authorization check
# HIPAA Rule: §164.312(d) - Person or entity authentication
@app.route("/patients", methods=["GET"])
def list_patients():
    db = get_db()
    patients = db.execute("SELECT * FROM patients").fetchall()
    result = [dict(row) for row in patients]
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #2: Logging raw PHI to console
    # HIPAA Rule: §164.312(b) - Audit controls
    logger.info(f"Retrieved patients: {result}")
    return jsonify(result)

@app.route("/patients/<int:patient_id>", methods=["GET"])
def get_patient(patient_id):
    db = get_db()
    patient = db.execute("SELECT * FROM patients WHERE id = ?", (patient_id,)).fetchone()
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    patient_data = dict(patient)
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #3: Logging SSN in plaintext
    # HIPAA Rule: §164.312(b) - Audit controls
    logger.info(f"Accessed patient {patient_data['full_name']} SSN: {patient_data['ssn']}")
    return jsonify(patient_data)

@app.route("/patients", methods=["POST"])
def create_patient():
    data = request.json
    db = get_db()
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #1 continued: No input validation, no encryption before storage
    db.execute(
        "INSERT INTO patients (full_name, ssn, date_of_birth, medical_record_number, diagnosis, phone_number, email, address) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (data["full_name"], data["ssn"], data["date_of_birth"], data["medical_record_number"], data["diagnosis"], data["phone_number"], data["email"], data["address"])
    )
    db.commit()
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #2 & #3: Returning raw SSN in response and logging it
    logger.info(f"Created patient: {data['full_name']}, SSN: {data['ssn']}")
    return jsonify({"message": "Patient created", "ssn": data["ssn"]}), 201

# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation: Transmitting PHI over HTTP (no TLS enforcement)
# HIPAA Rule: §164.312(e)(1) - Transmission security
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5001, debug=True)
