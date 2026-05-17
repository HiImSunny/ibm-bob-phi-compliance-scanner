# PRD: PHI Compliance Scanner — "Turn Idea into Impact Faster"

---

## Problem Statement

Healthcare devs deploying fixes to EHR systems must manually trace Protected Health Information (PHI) flows across dozens of microservices before each release — a process that takes days and is error-prone. A single missed PHI exposure can trigger HIPAA violations, audit failures, and patient data breaches. There is no automated, repo-aware tool that understands the full codebase context and generates compliant patches with tests in one pass.

---

## Solution Overview — What Bob Does

Bob acts as a repo-level HIPAA compliance agent. Given a target codebase, Bob:

1. **Scans** the entire repo for PHI patterns (SSN, DOB, MRN, diagnosis codes) across all files, configs, logs, and API schemas.
2. **Maps** the PHI data flow graph — which services touch, store, or transmit PHI and how.
3. **Generates** HIPAA-safe patches: encryption wrappers, access-control guards, and audit-log hooks injected at the right locations.
4. **Writes** unit + integration tests for every patched function to prove compliance.
5. **Produces** a one-page audit artifact (JSON + Markdown) ready for a compliance officer to sign off.

Bob's unique advantage: it holds the full repo in context, so it catches cross-service PHI leaks that file-by-file linters miss entirely.

---

## Tech Stack

| Layer | Choice |
|---|---|
| Language | Python 3.11 (backend scanner) + React/TS (demo UI) |
| AI IDE | IBM Bob (repo-level agent, custom rules file) |
| LLM / Analysis | watsonx.ai (granite-13b-instruct) for PHI classification |
| PHI Pattern Engine | Python `re` + custom HIPAA regex library |
| Test Generation | Bob agent → pytest scaffolding |
| Audit Report | Jinja2 → Markdown/JSON output |
| Sample Repo | Synthetic EHR microservices repo (3 services, ~500 LOC) |

---

## Demo Flow (3 minutes)

**Step 1 — Setup (0:00–0:20)**
Open the synthetic EHR repo in Bob IDE. Show 3 microservices: `patient-api`, `billing-service`, `audit-logger`. Point out that PHI is scattered and unguarded.

**Step 2 — Trigger Bob (0:20–0:50)**
Type in Bob: `"Scan this repo for HIPAA PHI violations and generate compliant patches."`
Bob reads the full repo, calls watsonx to classify ambiguous fields, builds the PHI flow graph live on screen.

**Step 3 — Review findings (0:50–1:30)**
Bob surfaces a findings panel: 7 violations found across 3 files. Highlight the worst one — raw SSN logged in `audit-logger/logger.py`. Bob explains the risk in plain English.

**Step 4 — Apply patches (1:30–2:10)**
One click: Bob applies all patches — encryption wrapper on SSN field, role-based access guard on `/patient` endpoint, redaction in log output. Show the diff in the IDE.

**Step 5 — Tests + Audit artifact (2:10–2:50)**
Bob auto-generates pytest cases for each patched function. Run tests — all green. Bob exports `audit-report.md` with violation list, patches applied, and test results. Ready to hand to compliance officer.

**Step 6 — Close (2:50–3:00)**
"What took a compliance team 3 days now takes 3 minutes. Idea to impact, faster."

---

## 5-Slide Submission Outline

**Slide 1 — The Problem**
- Stat: average HIPAA breach costs $1.9M; root cause is untracked PHI in code
- Visual: dev drowning in microservices, manual audit checklist
- Hook: "Your codebase is leaking patient data and you don't know where"

**Slide 2 — Meet Bob: Your Repo-Level Compliance Agent**
- What makes Bob different: full repo context vs. file-by-file linters
- One-sentence pitch: "Bob scans, patches, tests, and reports — in one command"
- Architecture diagram: Repo → Bob Agent → watsonx PHI classifier → Patches + Tests + Audit

**Slide 3 — Live Demo Highlights**
- Screenshot: PHI flow graph Bob generated
- Screenshot: diff view of Bob's patches
- Screenshot: green test run + audit-report.md

**Slide 4 — Impact**
- Time saved: 3 days → 3 minutes for PHI audit cycle
- Risk reduced: catches cross-service leaks no linter finds
- Scales to: any regulated codebase (GDPR, PCI-DSS, SOC2)

**Slide 5 — What's Next**
- CI/CD integration: Bob runs on every PR, blocks merge if PHI violation found
- Expand to HL7/FHIR schema validation
- Compliance dashboard for engineering managers

---

## Bob Custom Instructions (Rules File)

Save as `.bob/rules.md` in the project root:

```markdown
# Bob Rules — PHI Compliance Scanner Project

## Role
You are a HIPAA compliance engineering agent. Your primary job is to find,
explain, and fix Protected Health Information (PHI) violations in this codebase.

## PHI Definition (HIPAA 18 Identifiers)
Treat the following as PHI whenever found in code, configs, logs, or schemas:
- Names, geographic data, dates (except year), phone/fax, email, SSN
- Medical record numbers (MRN), health plan numbers, account numbers
- Certificate/license numbers, VINs, device identifiers, URLs, IP addresses
- Biometric identifiers, full-face photos, any unique identifying number

## Scanning Rules
- Always scan the ENTIRE repo, not just the file currently open.
- Check: source files, config files, .env examples, log outputs, API schemas,
  test fixtures, and migration scripts.
- Flag any variable name, string literal, or field name that matches PHI patterns.
- Flag any PHI transmitted over HTTP (not HTTPS) or stored without encryption.
- Flag any PHI written to logs without redaction.

## Patch Rules
- Never remove PHI handling — replace with compliant alternatives.
- Encryption: use AES-256 for PHI at rest; flag for TLS 1.2+ for PHI in transit.
- Logging: replace raw PHI with redacted tokens e.g. `SSN: ***-**-1234`.
- Access control: add role-check guard before any endpoint returning PHI.
- Always add an audit-log entry when PHI is accessed or modified.

## Test Generation Rules
- Write a pytest test for every function you patch.
- Tests must assert: (1) PHI is not exposed in output, (2) encrypted form is stored,
  (3) audit log entry is created on access.

## Audit Report Rules
- After scanning, generate `audit-report.md` at repo root.
- Include: total violations found, file + line for each, severity (Critical/High/Medium),
  patch applied (yes/no), test coverage (yes/no).
- Format must be readable by a non-technical compliance officer.

## Tone
- Explain violations in plain English, not just code references.
- Always state the HIPAA rule number being violated (e.g., 45 CFR §164.312).
- Be direct about severity — do not downplay Critical findings.
```

---

*PRD version 1.0 — IBM Bob Hackathon — May 2026*
