# Audit Logger Configuration
# WARNING: Contains intentional HIPAA violations for demo purposes

import os

# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation: No log retention policy - logs stored indefinitely
# HIPAA Rule: §164.316(b)(2)(i) - Retention of documentation
# Severity: Medium
# Issue: HIPAA requires "Retain documentation for 6 years from creation or last effective date"
# This configuration has no cleanup, no archival, no retention limits
LOG_RETENTION_DAYS = None  # Should be 2190 days (6 years)
LOG_CLEANUP_ENABLED = False
LOG_ARCHIVE_ENABLED = False

# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation: No audit trail for who accessed audit logs
# HIPAA Rule: §164.312(b) - Audit controls
# Severity: High
# Issue: Must log who accesses audit logs (audit the auditors)
AUDIT_LOG_ACCESS_TRACKING = False

# Log file configuration
LOG_FILE = os.getenv("AUDIT_LOG_FILE", "audit_events.log")
LOG_ENCRYPTION_ENABLED = False  # VIOLATION: Plaintext PHI in logs

# Export configuration
EXPORT_ENCRYPTION_ENABLED = False  # VIOLATION: Unencrypted exports
EXPORT_ACCESS_CONTROL = False  # VIOLATION: No auth on export endpoint

# Service configuration
HOST = "0.0.0.0"
PORT = 5003
DEBUG = True

# Made with Bob
