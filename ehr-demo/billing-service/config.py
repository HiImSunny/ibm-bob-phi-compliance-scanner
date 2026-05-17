# Billing Service Configuration
# WARNING: Contains intentional HIPAA violations for demo purposes

import os

# API endpoints
PATIENT_API_URL = "http://localhost:5001"  # VIOLATION: HTTP not HTTPS

# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation: No rate limiting on claim submission endpoint
# HIPAA Rule: §164.308(a)(1)(ii)(D) - Information system activity review
# Severity: Medium
# Issue: Allows bulk PHI extraction through repeated API calls
# Should implement: Rate limiting (e.g., 10 claims per minute per user)
RATE_LIMIT_ENABLED = False
RATE_LIMIT_CLAIMS_PER_MINUTE = 100  # Unrealistically high, effectively disabled

# Cache configuration
CLAIMS_CACHE_FILE = os.getenv("CACHE_FILE", "claims_cache.json")
CACHE_ENCRYPTION_ENABLED = False  # VIOLATION: Caching PHI without encryption

# Service configuration
HOST = "0.0.0.0"
PORT = 5002
DEBUG = True

# Made with Bob
