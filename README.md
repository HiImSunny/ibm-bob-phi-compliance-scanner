# PHI Compliance Scanner — IBM Bob Hackathon Project

**Theme**: Turn Idea into Impact Faster  
**Problem**: Healthcare devs spend days manually tracing PHI flows before each release  
**Solution**: Bob scans entire repo, auto-patches violations, generates tests + audit report in minutes

---

## Project Structure

```
IBM Bob Hackathon/
├── .bob/
│   └── rules.md                    # Bob's custom instructions for PHI scanning
├── ehr-demo/                       # Synthetic EHR system with intentional violations
│   ├── patient-api/                # Service 1: Patient CRUD (port 5001)
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── tests/
│   ├── billing-service/            # Service 2: Claims processing (port 5002)
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── tests/
│   ├── audit-logger/               # Service 3: Centralized logging (port 5003)
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── tests/
│   └── README.md
├── scanner/                        # PHI scanner implementation
│   ├── phi_scanner.py              # Main scanner engine
│   ├── phi_patterns.py             # HIPAA regex patterns
│   ├── patcher.py                  # Auto-patch generator
│   ├── test_generator.py           # Pytest test generator
│   ├── templates/                  # Jinja2 templates for reports
│   │   └── audit_report.md.j2
│   └── requirements.txt
├── reports/                        # Generated audit reports
│   └── (audit reports go here)
├── PRD-idea1-phi-scanner.md        # Product requirements doc
└── README.md                       # This file
```

---

## Quick Start

### 1. Run the vulnerable EHR demo
```bash
cd ehr-demo
pip install -r patient-api/requirements.txt
python patient-api/app.py &
python billing-service/app.py &
python audit-logger/app.py &
```

### 2. Run the PHI scanner
```bash
cd scanner
pip install -r requirements.txt
python phi_scanner.py --repo ../ehr-demo --output ../reports/audit-report.md
```

### 3. Let Bob do it for you
Open this repo in IBM Bob IDE and say:
```
"Scan ehr-demo for HIPAA PHI violations and generate compliant patches"
```

Bob will:
- Find all 10+ violations
- Generate patches with encryption + access control
- Write pytest tests
- Export audit report

---

## Demo Flow (3 minutes)

1. **Show the problem** (0:30) — Open `ehr-demo/audit-logger/app.py`, point to line 35 where raw SSN is logged
2. **Trigger Bob** (0:20) — Type the scan command
3. **Review findings** (0:40) — Bob shows 10 violations with severity + HIPAA rules
4. **Apply patches** (0:50) — One click, Bob fixes all violations
5. **Verify** (0:30) — Run tests, all green. Show `reports/audit-report.md`
6. **Impact** (0:10) — "3 days → 3 minutes"

---

## Key Files

- **`.bob/rules.md`** — Bob's instructions (PHI definitions, scanning rules, patch rules)
- **`PRD-idea1-phi-scanner.md`** — Full product requirements doc
- **`ehr-demo/`** — Synthetic vulnerable codebase for demo
- **`scanner/phi_scanner.py`** — Standalone Python scanner (works without Bob)

---

## Intentional Violations in ehr-demo

| # | File | Line | Violation | HIPAA Rule |
|---|------|------|-----------|------------|
| 1 | patient-api/app.py | 45 | SSN in plaintext DB | §164.312(a)(1) |
| 2 | patient-api/app.py | 52 | PHI logged to console | §164.312(b) |
| 3 | patient-api/app.py | 30 | No auth on /patients | §164.312(d) |
| 4 | billing-service/app.py | 28 | PHI in JSON file | §164.312(a)(1) |
| 5 | billing-service/app.py | 18 | HTTP not HTTPS | §164.312(e)(1) |
| 6 | billing-service/app.py | 42 | SSN in response | §164.502(b) |
| 7 | audit-logger/app.py | 35 | Raw SSN in logs | §164.312(b) |
| 8 | audit-logger/app.py | 48 | SSN in URL param | §164.312(e)(1) |
| 9 | audit-logger/app.py | 40 | No access control | §164.312(d) |
| 10 | audit-logger/app.py | 58 | Unencrypted export | §164.312(a)(1) |

---

## Tech Stack

- **Language**: Python 3.11
- **AI IDE**: IBM Bob (repo-level agent)
- **LLM**: watsonx.ai granite-13b-instruct (for PHI classification)
- **Web framework**: Flask 3.0
- **Testing**: pytest
- **Reporting**: Jinja2 templates

---

## Next Steps

- [ ] Integrate scanner into CI/CD pipeline
- [ ] Add FHIR/HL7 schema validation
- [ ] Build compliance dashboard UI
- [ ] Expand to GDPR, PCI-DSS, SOC2

---

## License

Demo project for IBM Bob Hackathon. Not for production use.
