# Audit Logger Service
# Centralized logging for all EHR system events
# WARNING: Contains intentional PHI violations for demo purposes

from flask import Flask, request, jsonify
import logging
import json
from datetime import datetime
import config

app = Flask(__name__)

# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation #11: Logging PHI to plaintext file with no encryption
# HIPAA Rule: §164.312(b) - Audit controls
LOG_FILE = "audit_events.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation #15: No log retention policy (stores indefinitely)
# HIPAA Rule: §164.316(b)(2)(i) - Retention of documentation
# Reference: See config.py - LOG_RETENTION_DAYS = None
# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation: In-memory store with raw PHI
audit_events = []

@app.route("/log", methods=["POST"])
def log_event():
    data = request.json
    event = {
        "timestamp": datetime.now().isoformat(),
        "event_type": data.get("event_type", "unknown"),
        "user_id": data.get("user_id"),
        # INTENTIONAL HIPAA VIOLATION FOR DEMO
        # Violation: Storing PHI identifiers in audit log
        "patient_name": data.get("patient_name"),  # Should be tokenized
        "patient_ssn": data.get("patient_ssn"),    # Should be redacted
        "patient_mrn": data.get("patient_mrn"),    # Should be hashed
        "action": data.get("action"),
        "details": data.get("details"),
        "ip_address": request.remote_addr          # IP is PHI under HIPAA
    }

    audit_events.append(event)

    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #11 continued: Writing full PHI to log file
    logger.info(f"AUDIT: {event['event_type']} | Patient: {event['patient_name']} | "
                f"SSN: {event['patient_ssn']} | MRN: {event['patient_mrn']} | "
                f"Action: {event['action']} | IP: {event['ip_address']}")

    return jsonify({"status": "logged", "event_id": len(audit_events)}), 201

@app.route("/logs", methods=["GET"])
def get_logs():
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #13: No access control, returns all PHI
    # HIPAA Rule: §164.312(d) - Person or entity authentication
    # Violation #16: No audit trail for who accessed logs
    # HIPAA Rule: §164.312(b) - Audit controls
    # Reference: See config.py - AUDIT_LOG_ACCESS_TRACKING = False
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation: No pagination, dumps everything
    return jsonify(audit_events)

@app.route("/logs/patient/<ssn>", methods=["GET"])
def get_patient_logs(ssn):
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #12: Using SSN as lookup key in URL (exposed in server logs)
    # HIPAA Rule: §164.312(e)(1) - Transmission security
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #13 continued: No authentication
    patient_events = [e for e in audit_events if e.get("patient_ssn") == ssn]
    logger.info(f"Log lookup for SSN: {ssn}, found {len(patient_events)} events")
    return jsonify(patient_events)

@app.route("/logs/export", methods=["GET"])
def export_logs():
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #14: Exporting all PHI without encryption or access control
    # HIPAA Rule: §164.312(a)(1) - Access control - encryption at rest
    # Reference: See config.py - EXPORT_ENCRYPTION_ENABLED = False
    export_data = {
        "exported_at": datetime.now().isoformat(),
        "total_events": len(audit_events),
        "events": audit_events
    }
    # INTENTIONAL HIPAA VIOLATION FOR DEMO
    # Violation #14 continued: Writing export to unencrypted file
    with open("audit_export.json", "w") as f:
        json.dump(export_data, f, indent=2)
    logger.info(f"Exported {len(audit_events)} audit events to file")
    return jsonify({"status": "exported", "file": "audit_export.json"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
