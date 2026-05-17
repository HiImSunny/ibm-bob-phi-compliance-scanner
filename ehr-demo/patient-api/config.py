# Patient API Configuration
# WARNING: Contains intentional HIPAA violations for demo purposes

import os

# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation: Hardcoded encryption key in source code
# HIPAA Rule: §164.312(a)(2)(iv) - Encryption and decryption key management
# Severity: Critical
# Issue: Encryption keys must be stored securely (HSM, key vault, env vars with restricted access)
# This key is visible to anyone with repo access
ENCRYPTION_KEY = "my-secret-key-12345-hardcoded-in-source"

# Database configuration
DATABASE_PATH = os.getenv("DB_PATH", "patients.db")

# API configuration
HOST = "0.0.0.0"
PORT = 5001
DEBUG = True  # VIOLATION: Debug mode in production exposes stack traces with PHI

# Logging configuration
LOG_LEVEL = "INFO"
LOG_PHI = True  # VIOLATION: Flag that enables PHI logging

# Made with Bob
