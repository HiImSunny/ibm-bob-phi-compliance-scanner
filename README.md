# PHI Compliance Scanner: Repo-Level HIPAA Violations Detection & Auto-Patching

**Scan entire healthcare codebases for HIPAA violations, auto-patch with encryption + access control, generate audit-ready reports — powered by IBM Bob.**

---

## Problem

Healthcare teams manually audit codebases for Protected Health Information (PHI) violations before each release — a process taking 3–5 days that still misses cross-service leaks. File-by-file linters cannot see the full data flow across microservices, and compliance officers lack technical context to validate fixes. A single missed PHI exposure (raw SSN in logs, unencrypted transmission, missing auth) triggers HIPAA violations, audit failures, and $1.9M+ breach costs.

---

## Solution

This project demonstrates **IBM Bob as a repo-level HIPAA compliance agent**. Bob scans entire codebases for all 18 HIPAA identifiers (SSN, MRN, DOB, phone, email, diagnosis codes, etc.), maps PHI data flows across services, auto-generates compliant patches (encryption, access control, redaction), writes pytest tests, and exports compliance-ready audit reports — all in one command. Bob's full-repo context catches cross-service leaks that traditional linters miss.

---

## How IBM Bob Helps

- **Scanning phase**: Bob reads all files (Python, JS, SQL, YAML, configs, logs) and detects 85+ PHI violations across 3 microservices using HIPAA regex patterns + watsonx.ai classification
- **Analysis phase**: Bob builds a PHI flow graph showing which services touch which data types, identifying cross-service exposure risks
- **Patching phase**: Bob generates surgical fixes — AES-256 encryption wrappers, `@require_auth` decorators, SSN redaction in logs (`***-**-1234`), TLS enforcement
- **Testing phase**: Bob auto-generates pytest stubs for every patched function, asserting PHI is not exposed, encrypted form is stored, audit logs are created
- **Reporting phase**: Bob exports `audit-report.md` (compliance-officer-ready) + `audit-report.json` (machine-readable) with violation severity, HIPAA rule numbers, patches applied, test coverage

---

## Architecture & Flow

```
Developer input:
"Scan this repo for HIPAA PHI violations and fix them"
                    ↓
        ┌───────────────────────┐
        │   IBM Bob IDE Agent   │  ← holds full repo context
        └───────────┬───────────┘
                    ↓
    ┌───────────────────────────────────┐
    │  PHI Scanner Engine               │
    │  - Regex patterns (SSN, MRN, etc) │
    │  - Log detection                  │
    │  - HTTP/HTTPS checks              │
    │  - File write detection           │
    └───────────┬───────────────────────┘
                ↓
    ┌───────────────────────────────────┐
    │  watsonx.ai granite-13b-instruct  │  ← PHI classification
    └───────────┬───────────────────────┘
                ↓
    ┌───────────────────────────────────┐
    │  Auto-Patcher                     │
    │  - Encryption wrappers (AES-256)  │
    │  - Access control decorators      │
    │  - Log redaction                  │
    │  - TLS enforcement                │
    └───────────┬───────────────────────┘
                ↓
    ┌───────────────────────────────────┐
    │  Test Generator                   │
    │  - pytest stubs per violation     │
    │  - PHI exposure assertions        │
    │  - Audit log verification         │
    └───────────┬───────────────────────┘
                ↓
    ┌───────────────────────────────────┐
    │  Audit Report Export              │
    │  - Markdown (human-readable)      │
    │  - JSON (machine-readable)        │
    │  - Sign-off checklist             │
    └───────────────────────────────────┘
```

**Key flow steps:**
- Scan entire repo (not file-by-file) to catch cross-service PHI flows
- Classify ambiguous fields using LLM (e.g., is `patient_id` PHI? context matters)
- Generate minimal, surgical patches (no code removal, only replacement)
- Test every patch before export
- Produce compliance-ready artifacts for sign-off

---

## How to Run

### 1. Standalone Scanner (no Bob IDE required)

```bash
cd scanner
pip install -r requirements.txt
python phi_scanner.py --repo ../ehr-demo --output ../reports/audit-report.md
```

**Output:**
- `reports/audit-report.md` — human-readable compliance report
- `reports/audit-report.json` — machine-readable violations data
- Console: PHI flow map + violation summary

### 2. With IBM Bob IDE

Open this repo in IBM Bob IDE and type:
```
"Scan ehr-demo for HIPAA PHI violations and generate compliant patches"
```

Bob will:
- Find all violations with HIPAA rule references
- Apply patches with diffs
- Generate tests
- Export audit report

### 3. Demo the Vulnerable EHR System

```bash
cd ehr-demo
pip install -r patient-api/requirements.txt
python patient-api/app.py &      # port 5001
python billing-service/app.py &  # port 5002
python audit-logger/app.py &     # port 5003
```

Then run scanner against it to see 85+ violations detected.

### Requirements

- Python 3.11+
- Flask 3.0, requests, Jinja2, pytest
- IBM Bob IDE (optional, for full agent experience)
- watsonx.ai API key (optional, for LLM-based classification)

---

## Repo Structure

```
ibm-bob-phi-compliance-scanner/
├── .bob/
│   └── rules.md                    # Bob's custom instructions (PHI defs, scanning/patching rules)
├── ehr-demo/                       # Synthetic vulnerable EHR system (3 microservices)
│   ├── patient-api/                # Service 1: Patient CRUD (plaintext DB, no auth)
│   │   ├── app.py                  # 10+ intentional violations
│   │   ├── requirements.txt
│   │   └── tests/
│   ├── billing-service/            # Service 2: Claims (PHI in JSON cache, HTTP)
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── tests/
│   ├── audit-logger/               # Service 3: Logging (raw SSN in logs, no access control)
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── tests/
│   └── README.md
├── scanner/                        # PHI scanner implementation
│   ├── phi_scanner.py              # Main engine (~400 LOC)
│   ├── phi_patterns.py             # HIPAA regex patterns (18 identifiers)
│   ├── test_generator.py           # Auto-generates pytest stubs
│   ├── requirements.txt
│   └── generated_tests/            # Output test files
├── reports/                        # Generated audit reports
│   ├── audit-report.md             # Compliance-ready report
│   └── audit-report.json           # Machine-readable violations
├── bob_sessions/                   # Evidence of Bob IDE usage (see below)
├── PRD-idea1-phi-scanner.md        # Full product requirements
├── slides-content.md               # 5-slide hackathon submission
└── README.md                       # This file
```

---

## Bob Sessions: Evidence of IBM Bob Usage

The `bob_sessions/` directory contains timestamped records of Bob IDE interactions during development:

| Session | File | Purpose |
|---------|------|---------|
| **00-init** | `00-init-history.md` + `.png` | Bob scaffolded project structure, created PRD outline |
| **01-ehr-demo** | `01-ehr-demo-history.md` + `.png` | Bob generated 3 vulnerable microservices with intentional violations |
| **02-scanner** | `02-scanner-history.md` + `.png` | Bob wrote PHI scanner engine, regex patterns, flow graph logic |
| **03-tests** | `03-tests-history.md` + `.png` | Bob generated pytest test stubs and audit report templates |
| **04-final-review** | `04-final-review-history.md` + `.png` | Bob reviewed code, optimized patterns, finalized reports |

Each session includes:
- **`*-history.md`** — Conversation transcript showing Bob's reasoning and code generation
- **`*-summary.png`** — Screenshot of Bob IDE with generated code visible

These files demonstrate that **IBM Bob was used as a co-developer throughout the hackathon**, not just for final polish. Bob handled:
- Architecture design (repo structure, microservice layout)
- Code generation (scanner engine, test stubs, report templates)
- Compliance logic (HIPAA rule mapping, violation classification)
- Optimization (regex performance, cross-service flow analysis)

---

## Key Metrics

| Metric | Value |
|--------|-------|
| **Violations detected** | 85 across 3 services |
| **PHI types covered** | 9 (SSN, MRN, DOB, phone, email, name, address, IP, diagnosis) |
| **HIPAA rules mapped** | 8 (§164.312(a)(1), §164.312(b), §164.312(d), §164.312(e)(1), §164.502(b)) |
| **Scanner LOC** | ~400 (Python) |
| **Test cases generated** | 34 pytest stubs |
| **Time to scan + patch** | < 5 minutes (vs. 3–5 days manual) |
| **Build time** | 6 hours (with Bob IDE) |

---

## Tech Stack

- **Language**: Python 3.11
- **AI IDE**: IBM Bob (repo-level agent with full codebase context)
- **LLM**: watsonx.ai granite-13b-instruct (PHI classification)
- **Web framework**: Flask 3.0 (demo EHR services)
- **Testing**: pytest (auto-generated compliance tests)
- **Reporting**: Jinja2 templates → Markdown/JSON
- **Pattern matching**: Python `re` + custom HIPAA regex library

---

## Next Steps

- **CI/CD integration**: Bob runs on every PR, blocks merge if Critical violations found
- **FHIR/HL7 validation**: Extend scanner to validate healthcare data exchange schemas
- **Compliance dashboard**: Real-time violation tracking across teams
- **Expand scope**: GDPR, PCI-DSS, SOC2 compliance scanning

---

## For Judges

**What makes this unique:**
- **Repo-level context**: Bob sees entire codebase at once, catches cross-service PHI leaks file-by-file linters miss
- **Full SDLC coverage**: Scan → patch → test → report in one workflow
- **Compliance-ready output**: Audit reports with HIPAA rule numbers, ready for sign-off
- **Demonstrated with Bob**: `bob_sessions/` shows Bob was used as co-developer, not just a tool

**Try it:**
```bash
python scanner/phi_scanner.py --repo ./ehr-demo --output ./reports/audit-report.md
```

Then open `reports/audit-report.md` to see 85 violations with severity, HIPAA rules, and recommended patches.

---

*IBM Bob Hackathon 2026 — "Turn Idea into Impact Faster"*
