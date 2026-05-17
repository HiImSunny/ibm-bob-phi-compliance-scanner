# EHR Demo — Synthetic Healthcare Microservices

A deliberately vulnerable EHR system with **intentional HIPAA/PHI violations** for demonstrating IBM Bob's compliance scanning capabilities.

## Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌────────────────┐
│  patient-api    │────▶│ billing-service  │────▶│  audit-logger  │
│  :5001          │     │  :5002           │     │  :5003         │
│                 │     │                  │     │                │
│ SQLite (plain)  │     │ JSON file cache  │     │ Plaintext logs │
└─────────────────┘     └──────────────────┘     └────────────────┘
```

## Intentional Violations (for demo)

All violations are clearly marked with `# INTENTIONAL HIPAA VIOLATION FOR DEMO` comments in the code.

| # | Service | Violation | HIPAA Rule | Severity |
|---|---------|-----------|------------|----------|
| 1 | patient-api | SSN stored in plaintext DB | §164.312(a)(1) | Critical |
| 2 | patient-api | PHI logged to console | §164.312(b) | Critical |
| 3 | patient-api | SSN logged in plaintext | §164.312(b) | Critical |
| 4 | patient-api | No auth on endpoints | §164.312(d) | High |
| 5 | patient-api | Hardcoded encryption key in config | §164.312(a)(2)(iv) | Critical |
| 6 | billing-service | HTTP (not HTTPS) calls | §164.312(e)(1) | Critical |
| 7 | billing-service | PHI cached in JSON file | §164.312(a)(1) | Critical |
| 8 | billing-service | SSN in claim (minimum necessary) | §164.502(b) | High |
| 9 | billing-service | Full PHI logged | §164.312(b) | High |
| 10 | billing-service | No rate limiting on claims | §164.308(a)(1)(ii)(D) | Medium |
| 11 | audit-logger | PHI in plaintext log file | §164.312(b) | Critical |
| 12 | audit-logger | SSN used as URL param | §164.312(e)(1) | Critical |
| 13 | audit-logger | No access control on /logs | §164.312(d) | Critical |
| 14 | audit-logger | Unencrypted export file | §164.312(a)(1) | Critical |
| 15 | audit-logger | No log retention policy | §164.316(b)(2)(i) | Medium |
| 16 | audit-logger | No audit trail for log access | §164.312(b) | High |
| 17 | shared | Weak PHI masking function | §164.514(b)(2) | Medium |

**Total: 17 intentional violations across 4 components**

## Running Locally

### Option 1: Manual Start
```bash
# Install dependencies
pip install -r patient-api/requirements.txt
pip install -r billing-service/requirements.txt
pip install -r audit-logger/requirements.txt

# Start services (in separate terminals)
python patient-api/app.py      # Port 5001
python billing-service/app.py  # Port 5002
python audit-logger/app.py     # Port 5003
```

### Option 2: Docker Compose (recommended)
```bash
docker-compose up
```

## Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest ehr-demo/

# Run tests for specific service
pytest ehr-demo/patient-api/tests/
pytest ehr-demo/billing-service/tests/
pytest ehr-demo/audit-logger/tests/

# Run with coverage
pytest --cov=ehr-demo --cov-report=html
```

**Note**: Tests are designed to PASS, proving violations exist. This is intentional for demo purposes.

## Project Structure

```
ehr-demo/
├── patient-api/          # Patient records service
│   ├── app.py           # 5 violations
│   ├── config.py        # Configuration violations
│   └── tests/           # Unit & integration tests
├── billing-service/      # Claims processing service
│   ├── app.py           # 5 violations
│   ├── config.py        # Configuration violations
│   └── tests/           # Unit & integration tests
├── audit-logger/         # Centralized audit logging
│   ├── app.py           # 6 violations
│   ├── config.py        # Configuration violations
│   └── tests/           # Unit & integration tests
└── shared/               # Shared utilities
    ├── phi_utils.py     # Weak PHI masking (1 violation)
    └── test_data.py     # Synthetic data generator
```

## Purpose

This repo exists solely to demonstrate Bob's PHI scanning and auto-patching capabilities.
**Do NOT deploy this code in any real environment.**

All data is synthetic. No real PHI is used.
