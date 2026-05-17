# HIPAA PHI Compliance Audit Report

**Generated**: 2026-05-17 14:43:54  
**Repository**: `D:\Code Project\Python Coding\IBM Bob Hackathon\ehr-demo`  
**Scanned files**: 28  
**Violations found**: 285  

---

## Executive Summary

Automated PHI scan identified **285 violations** across 28 files: 116 Critical, 128 High, 41 Medium. Immediate remediation required for Critical violations before next deployment. All violations must be resolved to achieve HIPAA compliance.

---

## Violations by Severity

### Critical (116)

- [ ] `README.md:22` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `| 1 | patient-api | SSN stored in plaintext DB | §164.312(a)(1) | Critical |`

- [ ] `README.md:24` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `| 3 | patient-api | SSN logged in plaintext | §164.312(b) | Critical |`

- [ ] `README.md:29` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `| 8 | billing-service | SSN in claim (minimum necessary) | §164.502(b) | High |`

- [ ] `README.md:33` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `| 12 | audit-logger | SSN used as URL param | §164.312(e)(1) | Critical |`

- [ ] `audit-logger\app.py:53` — **PHI in log: Patient Name** — §164.312(b)
  - Raw Patient Name written to log output — must be redacted
  - Code: `logger.info(f"AUDIT: {event['event_type']} | Patient: {event['patient_name']} | "`

- [ ] `audit-logger\app.py:54` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `f"SSN: {event['patient_ssn']} | MRN: {event['patient_mrn']} | "`

- [ ] `audit-logger\app.py:54` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `f"SSN: {event['patient_ssn']} | MRN: {event['patient_mrn']} | "`

- [ ] `audit-logger\app.py:71` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `@app.route("/logs/patient/<ssn>", methods=["GET"])`

- [ ] `audit-logger\app.py:72` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `def get_patient_logs(ssn):`

- [ ] `audit-logger\app.py:78` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `patient_events = [e for e in audit_events if e.get("patient_ssn") == ssn]`

- [ ] `audit-logger\app.py:79` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `logger.info(f"Log lookup for SSN: {ssn}, found {len(patient_events)} events")`

- [ ] `audit-logger\app.py:79` — **PHI in log: Social Security Number** — §164.312(b)
  - Raw Social Security Number written to log output — must be redacted
  - Code: `logger.info(f"Log lookup for SSN: {ssn}, found {len(patient_events)} events")`

- [ ] `audit-logger\tests\test_audit_logger.py:34` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"patient_ssn": "123-45-6789",`

- [ ] `audit-logger\tests\test_audit_logger.py:35` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"patient_mrn": "MRN-001234",`

- [ ] `audit-logger\tests\test_audit_logger.py:46` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert event['patient_ssn'] == "123-45-6789", "SSN should be redacted but isn't"`

- [ ] `audit-logger\tests\test_audit_logger.py:59` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"patient_ssn": "111-11-1111",`

- [ ] `audit-logger\tests\test_audit_logger.py:60` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"patient_mrn": "MRN-001",`

- [ ] `audit-logger\tests\test_audit_logger.py:68` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"patient_ssn": "222-22-2222",`

- [ ] `audit-logger\tests\test_audit_logger.py:69` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"patient_mrn": "MRN-002",`

- [ ] `audit-logger\tests\test_audit_logger.py:86` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert data[0]['patient_ssn'] == "111-11-1111"`

- [ ] `audit-logger\tests\test_audit_logger.py:87` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert data[1]['patient_ssn'] == "222-22-2222"`

- [ ] `audit-logger\tests\test_audit_logger.py:91` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `VIOLATION TEST: Verify SSN is used in URL path (exposed in server logs)`

- [ ] `audit-logger\tests\test_audit_logger.py:98` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"patient_ssn": "999-88-7777",`

- [ ] `audit-logger\tests\test_audit_logger.py:99` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"patient_mrn": "MRN-URL",`

- [ ] `audit-logger\tests\test_audit_logger.py:106` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `response = client.get('/logs/patient/999-88-7777')`

- [ ] `audit-logger\tests\test_audit_logger.py:111` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert data[0]['patient_ssn'] == "999-88-7777"`

- [ ] `audit-logger\tests\test_audit_logger.py:122` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"patient_ssn": "555-66-7777",`

- [ ] `audit-logger\tests\test_audit_logger.py:123` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"patient_mrn": "MRN-EXPORT",`

- [ ] `audit-logger\tests\test_audit_logger.py:141` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert export_data['events'][0]['patient_ssn'] == "555-66-7777"`

- [ ] `audit-logger\tests\test_audit_logger.py:165` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"patient_ssn": "444-55-6666",`

- [ ] `audit-logger\tests\test_audit_logger.py:166` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"patient_mrn": "MRN-AUDIT",`

- [ ] `audit-logger\tests\test_integration.py:31` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"patient_ssn": "777-88-9999",`

- [ ] `audit-logger\tests\test_integration.py:32` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"patient_mrn": "MRN-FILE",`

- [ ] `audit-logger\tests\test_integration.py:47` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert "777-88-9999" in log_content, "SSN should be redacted but is in plaintext log"`

- [ ] `audit-logger\tests\test_integration.py:61` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"patient_mrn": f"MRN-{i:03d}",`

- [ ] `audit-logger\tests\test_integration.py:83` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"patient_ssn": "888-99-0000",`

- [ ] `audit-logger\tests\test_integration.py:84` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"patient_mrn": "MRN-IP",`

- [ ] `audit-logger\tests\test_integration.py:106` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"patient_ssn": "666-77-8888",`

- [ ] `audit-logger\tests\test_integration.py:107` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"patient_mrn": "MRN-TRAIL",`

- [ ] `audit-logger\tests\test_integration.py:117` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `client.get('/logs/patient/666-77-8888')`

- [ ] `audit_events.log:4` — **Unencrypted HTTP transmission** — §164.312(e)(1)
  - PHI transmitted over HTTP — must use HTTPS (TLS 1.2+)
  - Code: `* Running on http://10.161.218.8:5003`

- [ ] `billing-service\app.py:58` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"patient_ssn": patient["ssn"],`

- [ ] `billing-service\app.py:90` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `logger.info(f"Claim accessed: {claim['patient_name']} SSN:{claim['patient_ssn']}")`

- [ ] `billing-service\app.py:90` — **PHI in log: Social Security Number** — §164.312(b)
  - Raw Social Security Number written to log output — must be redacted
  - Code: `logger.info(f"Claim accessed: {claim['patient_name']} SSN:{claim['patient_ssn']}")`

- [ ] `billing-service\app.py:102` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `patient_claims = [c for c in claims if c["patient_ssn"] == patient["ssn"]]`

- [ ] `billing-service\app.py:105` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `logger.info(f"Claims lookup for SSN: {patient['ssn']} found {len(patient_claims)} claims")`

- [ ] `billing-service\app.py:105` — **PHI in log: Social Security Number** — §164.312(b)
  - Raw Social Security Number written to log output — must be redacted
  - Code: `logger.info(f"Claims lookup for SSN: {patient['ssn']} found {len(patient_claims)} claims")`

- [ ] `billing-service\tests\test_billing_service.py:35` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"ssn": "123-45-6789",`

- [ ] `billing-service\tests\test_billing_service.py:37` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"medical_record_number": "MRN-001234"`

- [ ] `billing-service\tests\test_billing_service.py:42` — **Unencrypted HTTP transmission** — §164.312(e)(1)
  - PHI transmitted over HTTP — must use HTTPS (TLS 1.2+)
  - Code: `assert url.startswith("http://"), "Should use HTTPS but uses HTTP"`

- [ ] `billing-service\tests\test_billing_service.py:61` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `VIOLATION TEST: Verify SSN is stored in plaintext cache file`

- [ ] `billing-service\tests\test_billing_service.py:69` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"ssn": "999-88-7777",`

- [ ] `billing-service\tests\test_billing_service.py:71` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"medical_record_number": "MRN-TEST"`

- [ ] `billing-service\tests\test_billing_service.py:96` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert claim['patient_ssn'] == "999-88-7777", "SSN should be encrypted but is plaintext"`

- [ ] `billing-service\tests\test_billing_service.py:108` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"ssn": "111-22-3333",`

- [ ] `billing-service\tests\test_billing_service.py:110` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"medical_record_number": "MRN-001"`

- [ ] `billing-service\tests\test_billing_service.py:139` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"ssn": "555-66-7777",`

- [ ] `billing-service\tests\test_billing_service.py:141` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"medical_record_number": "MRN-XYZ"`

- [ ] `billing-service\tests\test_integration.py:33` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"ssn": "888-99-0000",`

- [ ] `billing-service\tests\test_integration.py:35` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"medical_record_number": "MRN-CROSS",`

- [ ] `billing-service\tests\test_integration.py:56` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert claim['patient_ssn'] == "888-99-0000"`

- [ ] `billing-service\tests\test_integration.py:68` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"ssn": "777-88-9999",`

- [ ] `billing-service\tests\test_integration.py:70` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"medical_record_number": "MRN-CACHE"`

- [ ] `billing-service\tests\test_integration.py:93` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert "777-88-9999" in content, "SSN should be encrypted but is plaintext in cache"`

- [ ] `billing-service\tests\test_integration.py:108` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"ssn": "666-77-8888",`

- [ ] `billing-service\tests\test_integration.py:110` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"medical_record_number": "MRN-LOG"`

- [ ] `billing-service\tests\test_integration.py:129` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert "666-77-8888" in log_output or "Log Test" in log_output, "PHI should not be in logs"`

- [ ] `docker-compose.yml:31` — **Unencrypted HTTP transmission** — §164.312(e)(1)
  - PHI transmitted over HTTP — must use HTTPS (TLS 1.2+)
  - Code: `- PATIENT_API_URL=http://patient-api:5001`

- [ ] `patient-api\app.py:34` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `ssn TEXT,`

- [ ] `patient-api\app.py:36` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `medical_record_number TEXT,`

- [ ] `patient-api\app.py:46` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `INSERT OR IGNORE INTO patients (id, full_name, ssn, date_of_birth, medical_record_number, diagnosis,`

- [ ] `patient-api\app.py:46` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `INSERT OR IGNORE INTO patients (id, full_name, ssn, date_of_birth, medical_record_number, diagnosis,`

- [ ] `patient-api\app.py:47` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `VALUES (1, 'John Smith', '123-45-6789', '1985-03-15', 'MRN-001234', 'Type 2 Diabetes', '555-0123', '`

- [ ] `patient-api\app.py:47` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `VALUES (1, 'John Smith', '123-45-6789', '1985-03-15', 'MRN-001234', 'Type 2 Diabetes', '555-0123', '`

- [ ] `patient-api\app.py:75` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `logger.info(f"Accessed patient {patient_data['full_name']} SSN: {patient_data['ssn']}")`

- [ ] `patient-api\app.py:75` — **PHI in log: Social Security Number** — §164.312(b)
  - Raw Social Security Number written to log output — must be redacted
  - Code: `logger.info(f"Accessed patient {patient_data['full_name']} SSN: {patient_data['ssn']}")`

- [ ] `patient-api\app.py:85` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"INSERT INTO patients (full_name, ssn, date_of_birth, medical_record_number, diagnosis, phone_number`

- [ ] `patient-api\app.py:85` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"INSERT INTO patients (full_name, ssn, date_of_birth, medical_record_number, diagnosis, phone_number`

- [ ] `patient-api\app.py:86` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `(data["full_name"], data["ssn"], data["date_of_birth"], data["medical_record_number"], data["diagnos`

- [ ] `patient-api\app.py:86` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `(data["full_name"], data["ssn"], data["date_of_birth"], data["medical_record_number"], data["diagnos`

- [ ] `patient-api\app.py:91` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `logger.info(f"Created patient: {data['full_name']}, SSN: {data['ssn']}")`

- [ ] `patient-api\app.py:91` — **PHI in log: Social Security Number** — §164.312(b)
  - Raw Social Security Number written to log output — must be redacted
  - Code: `logger.info(f"Created patient: {data['full_name']}, SSN: {data['ssn']}")`

- [ ] `patient-api\app.py:92` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `return jsonify({"message": "Patient created", "ssn": data["ssn"]}), 201`

- [ ] `patient-api\tests\test_integration.py:27` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"ssn": "111-22-3333",`

- [ ] `patient-api\tests\test_integration.py:29` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"medical_record_number": "MRN-INT001",`

- [ ] `patient-api\tests\test_integration.py:41` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `cursor = db.execute("SELECT ssn, full_name FROM patients WHERE ssn = ?", ("111-22-3333",))`

- [ ] `patient-api\tests\test_integration.py:46` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert row['ssn'] == "111-22-3333", "SSN should be encrypted but is plaintext"`

- [ ] `patient-api\tests\test_integration.py:63` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert 'SSN' in log_output or 'patient' in log_output.lower()`

- [ ] `patient-api\tests\test_patient_api.py:33` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert 'ssn' in patient, "SSN should be redacted but isn't"`

- [ ] `patient-api\tests\test_patient_api.py:38` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert '-' in patient['ssn'], "SSN is in plaintext format"`

- [ ] `patient-api\tests\test_patient_api.py:61` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert 'ssn' in data`

- [ ] `patient-api\tests\test_patient_api.py:62` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `assert 'medical_record_number' in data`

- [ ] `patient-api\tests\test_patient_api.py:72` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"ssn": "999-88-7777",`

- [ ] `patient-api\tests\test_patient_api.py:74` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"medical_record_number": "MRN-TEST001",`

- [ ] `patient-api\tests\test_patient_api.py:88` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `assert 'ssn' in data`

- [ ] `shared\phi_utils.py:12` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `def mask_ssn_weak(ssn):`

- [ ] `shared\phi_utils.py:14` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `Weakly mask SSN by showing last 4 digits.`

- [ ] `shared\phi_utils.py:17` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `if not ssn or len(ssn) < 4:`

- [ ] `shared\phi_utils.py:19` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `return f"***-**-{ssn[-4:]}"`

- [ ] `shared\phi_utils.py:35` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `def mask_mrn_weak(mrn):`

- [ ] `shared\phi_utils.py:37` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `Weakly mask MRN by showing last 3 digits.`

- [ ] `shared\phi_utils.py:40` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `if not mrn or len(mrn) < 3:`

- [ ] `shared\phi_utils.py:41` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `return "MRN-***"`

- [ ] `shared\phi_utils.py:42` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `return f"MRN-***{mrn[-3:]}"`

- [ ] `shared\phi_utils.py:49` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `def validate_ssn(ssn):`

- [ ] `shared\phi_utils.py:51` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `Validate SSN format.`

- [ ] `shared\phi_utils.py:52` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `VIOLATION: Logs invalid SSN attempts with actual SSN value.`

- [ ] `shared\phi_utils.py:55` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `if not re.match(pattern, ssn):`

- [ ] `shared\phi_utils.py:57` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `print(f"[VALIDATION ERROR] Invalid SSN format: {ssn}")`

- [ ] `shared\phi_utils.py:57` — **PHI in log: Social Security Number** — §164.312(b)
  - Raw Social Security Number written to log output — must be redacted
  - Code: `print(f"[VALIDATION ERROR] Invalid SSN format: {ssn}")`

- [ ] `shared\phi_utils.py:68` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `'ssn', 'social_security', 'social_security_number',`

- [ ] `shared\phi_utils.py:71` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `'mrn', 'medical_record', 'medical_record_number',`

- [ ] `shared\test_data.py:24` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"""Generate a fake SSN in format XXX-XX-XXXX"""`

- [ ] `shared\test_data.py:33` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `return f"MRN-{random.randint(100000, 999999)}"`

- [ ] `shared\test_data.py:64` — **Social Security Number** — §164.312(a)(1)
  - PHI field 'SSN' found in code without protection
  - Code: `"ssn": generate_ssn(),`

- [ ] `shared\test_data.py:66` — **Medical Record Number** — §164.312(a)(1)
  - PHI field 'MRN' found in code without protection
  - Code: `"medical_record_number": generate_mrn(),`

### High (128)

- [ ] `audit-logger\app.py:32` — **Endpoint missing authentication** — §164.312(d)
  - API endpoint has no authentication decorator — PHI accessible without credentials
  - Code: `@app.route("/log", methods=["POST"])`

- [ ] `audit-logger\app.py:41` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"patient_name": data.get("patient_name"),  # Should be tokenized`

- [ ] `audit-logger\app.py:53` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `logger.info(f"AUDIT: {event['event_type']} | Patient: {event['patient_name']} | "`

- [ ] `audit-logger\app.py:59` — **Endpoint missing authentication** — §164.312(d)
  - API endpoint has no authentication decorator — PHI accessible without credentials
  - Code: `@app.route("/logs", methods=["GET"])`

- [ ] `audit-logger\app.py:71` — **Endpoint missing authentication** — §164.312(d)
  - API endpoint has no authentication decorator — PHI accessible without credentials
  - Code: `@app.route("/logs/patient/<ssn>", methods=["GET"])`

- [ ] `audit-logger\app.py:82` — **Endpoint missing authentication** — §164.312(d)
  - API endpoint has no authentication decorator — PHI accessible without credentials
  - Code: `@app.route("/logs/export", methods=["GET"])`

- [ ] `audit-logger\tests\test_audit_logger.py:33` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"patient_name": "Test Patient",`

- [ ] `audit-logger\tests\test_audit_logger.py:47` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `assert event['patient_name'] == "Test Patient", "Name should be masked but isn't"`

- [ ] `audit-logger\tests\test_audit_logger.py:58` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"patient_name": "Patient One",`

- [ ] `audit-logger\tests\test_audit_logger.py:67` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"patient_name": "Patient Two",`

- [ ] `audit-logger\tests\test_audit_logger.py:97` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"patient_name": "URL Test",`

- [ ] `audit-logger\tests\test_audit_logger.py:121` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"patient_name": "Export Test",`

- [ ] `audit-logger\tests\test_audit_logger.py:164` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"patient_name": "Audit Test",`

- [ ] `audit-logger\tests\test_integration.py:30` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"patient_name": "File Test Patient",`

- [ ] `audit-logger\tests\test_integration.py:59` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"patient_name": f"Patient {i}",`

- [ ] `audit-logger\tests\test_integration.py:82` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"patient_name": "IP Test",`

- [ ] `audit-logger\tests\test_integration.py:105` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"patient_name": "Audit Trail Test",`

- [ ] `audit_events.log:1` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `2026-05-17 14:31:53,276 - INFO - [31m[1mWARNING: This is a development server. Do not use it in a `

- [ ] `audit_events.log:5` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `2026-05-17 14:31:53,277 - INFO - [33mPress CTRL+C to quit[0m`

- [ ] `audit_events.log:6` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `2026-05-17 14:31:53,283 - INFO -  * Restarting with stat`

- [ ] `audit_events.log:7` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `2026-05-17 14:31:53,831 - WARNING -  * Debugger is active!`

- [ ] `audit_events.log:8` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `2026-05-17 14:31:53,842 - INFO -  * Debugger PIN: 183-652-878`

- [ ] `billing-service\app.py:42` — **Endpoint missing authentication** — §164.312(d)
  - API endpoint has no authentication decorator — PHI accessible without credentials
  - Code: `@app.route("/claims", methods=["POST"])`

- [ ] `billing-service\app.py:54` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"patient_name": patient["full_name"],`

- [ ] `billing-service\app.py:59` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `"patient_dob": patient["date_of_birth"],`

- [ ] `billing-service\app.py:60` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `"diagnosis_code": data["diagnosis_code"],`

- [ ] `billing-service\app.py:80` — **Endpoint missing authentication** — §164.312(d)
  - API endpoint has no authentication decorator — PHI accessible without credentials
  - Code: `@app.route("/claims/<claim_id>", methods=["GET"])`

- [ ] `billing-service\app.py:90` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `logger.info(f"Claim accessed: {claim['patient_name']} SSN:{claim['patient_ssn']}")`

- [ ] `billing-service\app.py:94` — **Endpoint missing authentication** — §164.312(d)
  - API endpoint has no authentication decorator — PHI accessible without credentials
  - Code: `@app.route("/claims/patient/<int:patient_id>", methods=["GET"])`

- [ ] `billing-service\tests\test_billing_service.py:34` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"full_name": "Test Patient",`

- [ ] `billing-service\tests\test_billing_service.py:36` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `"date_of_birth": "1985-03-15",`

- [ ] `billing-service\tests\test_billing_service.py:50` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `"diagnosis_code": "E11.9",`

- [ ] `billing-service\tests\test_billing_service.py:68` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"full_name": "Test Patient",`

- [ ] `billing-service\tests\test_billing_service.py:70` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `"date_of_birth": "1990-01-01",`

- [ ] `billing-service\tests\test_billing_service.py:79` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `"diagnosis_code": "E11.9",`

- [ ] `billing-service\tests\test_billing_service.py:107` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"full_name": "Test Patient",`

- [ ] `billing-service\tests\test_billing_service.py:109` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `"date_of_birth": "1985-05-15",`

- [ ] `billing-service\tests\test_billing_service.py:118` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `"diagnosis_code": "E11.9",`

- [ ] `billing-service\tests\test_billing_service.py:138` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"full_name": "Test Patient",`

- [ ] `billing-service\tests\test_billing_service.py:140` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `"date_of_birth": "1980-12-25",`

- [ ] `billing-service\tests\test_billing_service.py:149` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `"diagnosis_code": "E11.9",`

- [ ] `billing-service\tests\test_billing_service.py:165` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `assert 'patient_name' in data`

- [ ] `billing-service\tests\test_integration.py:32` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"full_name": "Cross Service Test",`

- [ ] `billing-service\tests\test_integration.py:34` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `"date_of_birth": "1975-06-20",`

- [ ] `billing-service\tests\test_integration.py:36` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `"diagnosis": "Test Condition"`

- [ ] `billing-service\tests\test_integration.py:44` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `"diagnosis_code": "E11.9",`

- [ ] `billing-service\tests\test_integration.py:57` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `assert claim['patient_name'] == "Cross Service Test"`

- [ ] `billing-service\tests\test_integration.py:67` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"full_name": "Cache Test Patient",`

- [ ] `billing-service\tests\test_integration.py:69` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `"date_of_birth": "1988-08-08",`

- [ ] `billing-service\tests\test_integration.py:78` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `"diagnosis_code": "I10",`

- [ ] `billing-service\tests\test_integration.py:107` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"full_name": "Log Test",`

- [ ] `billing-service\tests\test_integration.py:109` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `"date_of_birth": "1992-03-10",`

- [ ] `billing-service\tests\test_integration.py:118` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `"diagnosis_code": "J45.9",`

- [ ] `patient-api\app.py:33` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `full_name TEXT,`

- [ ] `patient-api\app.py:35` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `date_of_birth TEXT,`

- [ ] `patient-api\app.py:37` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `diagnosis TEXT,`

- [ ] `patient-api\app.py:38` — **Phone Number** — §164.312(a)(1)
  - PHI field 'PHONE' found in code without protection
  - Code: `phone_number TEXT,`

- [ ] `patient-api\app.py:39` — **Email Address** — §164.312(a)(1)
  - PHI field 'EMAIL' found in code without protection
  - Code: `email TEXT,`

- [ ] `patient-api\app.py:46` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `INSERT OR IGNORE INTO patients (id, full_name, ssn, date_of_birth, medical_record_number, diagnosis,`

- [ ] `patient-api\app.py:46` — **Phone Number** — §164.312(a)(1)
  - PHI field 'PHONE' found in code without protection
  - Code: `INSERT OR IGNORE INTO patients (id, full_name, ssn, date_of_birth, medical_record_number, diagnosis,`

- [ ] `patient-api\app.py:46` — **Email Address** — §164.312(a)(1)
  - PHI field 'EMAIL' found in code without protection
  - Code: `INSERT OR IGNORE INTO patients (id, full_name, ssn, date_of_birth, medical_record_number, diagnosis,`

- [ ] `patient-api\app.py:46` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `INSERT OR IGNORE INTO patients (id, full_name, ssn, date_of_birth, medical_record_number, diagnosis,`

- [ ] `patient-api\app.py:46` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `INSERT OR IGNORE INTO patients (id, full_name, ssn, date_of_birth, medical_record_number, diagnosis,`

- [ ] `patient-api\app.py:47` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `VALUES (1, 'John Smith', '123-45-6789', '1985-03-15', 'MRN-001234', 'Type 2 Diabetes', '555-0123', '`

- [ ] `patient-api\app.py:47` — **Email Address** — §164.312(a)(1)
  - PHI field 'EMAIL' found in code without protection
  - Code: `VALUES (1, 'John Smith', '123-45-6789', '1985-03-15', 'MRN-001234', 'Type 2 Diabetes', '555-0123', '`

- [ ] `patient-api\app.py:54` — **Endpoint missing authentication** — §164.312(d)
  - API endpoint has no authentication decorator — PHI accessible without credentials
  - Code: `@app.route("/patients", methods=["GET"])`

- [ ] `patient-api\app.py:65` — **Endpoint missing authentication** — §164.312(d)
  - API endpoint has no authentication decorator — PHI accessible without credentials
  - Code: `@app.route("/patients/<int:patient_id>", methods=["GET"])`

- [ ] `patient-api\app.py:75` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `logger.info(f"Accessed patient {patient_data['full_name']} SSN: {patient_data['ssn']}")`

- [ ] `patient-api\app.py:78` — **Endpoint missing authentication** — §164.312(d)
  - API endpoint has no authentication decorator — PHI accessible without credentials
  - Code: `@app.route("/patients", methods=["POST"])`

- [ ] `patient-api\app.py:85` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `"INSERT INTO patients (full_name, ssn, date_of_birth, medical_record_number, diagnosis, phone_number`

- [ ] `patient-api\app.py:85` — **Phone Number** — §164.312(a)(1)
  - PHI field 'PHONE' found in code without protection
  - Code: `"INSERT INTO patients (full_name, ssn, date_of_birth, medical_record_number, diagnosis, phone_number`

- [ ] `patient-api\app.py:85` — **Email Address** — §164.312(a)(1)
  - PHI field 'EMAIL' found in code without protection
  - Code: `"INSERT INTO patients (full_name, ssn, date_of_birth, medical_record_number, diagnosis, phone_number`

- [ ] `patient-api\app.py:85` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"INSERT INTO patients (full_name, ssn, date_of_birth, medical_record_number, diagnosis, phone_number`

- [ ] `patient-api\app.py:85` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `"INSERT INTO patients (full_name, ssn, date_of_birth, medical_record_number, diagnosis, phone_number`

- [ ] `patient-api\app.py:86` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `(data["full_name"], data["ssn"], data["date_of_birth"], data["medical_record_number"], data["diagnos`

- [ ] `patient-api\app.py:86` — **Phone Number** — §164.312(a)(1)
  - PHI field 'PHONE' found in code without protection
  - Code: `(data["full_name"], data["ssn"], data["date_of_birth"], data["medical_record_number"], data["diagnos`

- [ ] `patient-api\app.py:86` — **Email Address** — §164.312(a)(1)
  - PHI field 'EMAIL' found in code without protection
  - Code: `(data["full_name"], data["ssn"], data["date_of_birth"], data["medical_record_number"], data["diagnos`

- [ ] `patient-api\app.py:86` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `(data["full_name"], data["ssn"], data["date_of_birth"], data["medical_record_number"], data["diagnos`

- [ ] `patient-api\app.py:86` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `(data["full_name"], data["ssn"], data["date_of_birth"], data["medical_record_number"], data["diagnos`

- [ ] `patient-api\app.py:91` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `logger.info(f"Created patient: {data['full_name']}, SSN: {data['ssn']}")`

- [ ] `patient-api\tests\test_integration.py:26` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"full_name": "Integration Test",`

- [ ] `patient-api\tests\test_integration.py:28` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `"date_of_birth": "1985-05-15",`

- [ ] `patient-api\tests\test_integration.py:30` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `"diagnosis": "Test Diagnosis",`

- [ ] `patient-api\tests\test_integration.py:31` — **Phone Number** — §164.312(a)(1)
  - PHI field 'PHONE' found in code without protection
  - Code: `"phone_number": "555-0100",`

- [ ] `patient-api\tests\test_integration.py:32` — **Email Address** — §164.312(a)(1)
  - PHI field 'EMAIL' found in code without protection
  - Code: `"email": "integration@test.com",`

- [ ] `patient-api\tests\test_integration.py:41` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `cursor = db.execute("SELECT ssn, full_name FROM patients WHERE ssn = ?", ("111-22-3333",))`

- [ ] `patient-api\tests\test_integration.py:47` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `assert row['full_name'] == "Integration Test", "Name should be encrypted but is plaintext"`

- [ ] `patient-api\tests\test_patient_api.py:34` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `assert 'date_of_birth' in patient, "DOB should be redacted but isn't"`

- [ ] `patient-api\tests\test_patient_api.py:35` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `assert 'full_name' in patient, "Full name should be masked but isn't"`

- [ ] `patient-api\tests\test_patient_api.py:63` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `assert 'diagnosis' in data`

- [ ] `patient-api\tests\test_patient_api.py:71` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"full_name": "Test Patient",`

- [ ] `patient-api\tests\test_patient_api.py:73` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `"date_of_birth": "1990-01-01",`

- [ ] `patient-api\tests\test_patient_api.py:75` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `"diagnosis": "Test Condition",`

- [ ] `patient-api\tests\test_patient_api.py:76` — **Phone Number** — §164.312(a)(1)
  - PHI field 'PHONE' found in code without protection
  - Code: `"phone_number": "555-0199",`

- [ ] `patient-api\tests\test_patient_api.py:77` — **Email Address** — §164.312(a)(1)
  - PHI field 'EMAIL' found in code without protection
  - Code: `"email": "test@example.com",`

- [ ] `shared\phi_utils.py:22` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `def mask_name_weak(full_name):`

- [ ] `shared\phi_utils.py:27` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `if not full_name:`

- [ ] `shared\phi_utils.py:29` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `parts = full_name.split()`

- [ ] `shared\phi_utils.py:69` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `'name', 'full_name', 'first_name', 'last_name',`

- [ ] `shared\phi_utils.py:70` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `'dob', 'date_of_birth', 'birth_date',`

- [ ] `shared\phi_utils.py:72` — **Phone Number** — §164.312(a)(1)
  - PHI field 'PHONE' found in code without protection
  - Code: `'phone', 'phone_number', 'telephone',`

- [ ] `shared\phi_utils.py:73` — **Email Address** — §164.312(a)(1)
  - PHI field 'EMAIL' found in code without protection
  - Code: `'email', 'email_address',`

- [ ] `shared\phi_utils.py:75` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `'diagnosis', 'condition', 'procedure',`

- [ ] `shared\test_data.py:36` — **Phone Number** — §164.312(a)(1)
  - PHI field 'PHONE' found in code without protection
  - Code: `"""Generate a fake phone number"""`

- [ ] `shared\test_data.py:45` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `dob = datetime.now() - timedelta(days=days_ago)`

- [ ] `shared\test_data.py:46` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `return dob.strftime("%Y-%m-%d")`

- [ ] `shared\test_data.py:59` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `first_name = random.choice(FIRST_NAMES)`

- [ ] `shared\test_data.py:60` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `last_name = random.choice(LAST_NAMES)`

- [ ] `shared\test_data.py:63` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"full_name": f"{first_name} {last_name}",`

- [ ] `shared\test_data.py:65` — **Date of Birth** — §164.312(a)(1)
  - PHI field 'DOB' found in code without protection
  - Code: `"date_of_birth": generate_dob(),`

- [ ] `shared\test_data.py:67` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `"diagnosis": random.choice(DIAGNOSES),`

- [ ] `shared\test_data.py:68` — **Phone Number** — §164.312(a)(1)
  - PHI field 'PHONE' found in code without protection
  - Code: `"phone_number": generate_phone(),`

- [ ] `shared\test_data.py:69` — **Email Address** — §164.312(a)(1)
  - PHI field 'EMAIL' found in code without protection
  - Code: `"email": f"{first_name.lower()}.{last_name.lower()}@email.com",`

- [ ] `shared\test_data.py:69` — **Patient Name** — §164.312(a)(1)
  - PHI field 'NAME' found in code without protection
  - Code: `"email": f"{first_name.lower()}.{last_name.lower()}@email.com",`

- [ ] `test_billing-service_app_py.py:499` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `Violation: Diagnosis / ICD Code`

- [ ] `test_patient-api_app_py.py:915` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `Violation: Diagnosis / ICD Code`

- [ ] `test_patient-api_app_py.py:967` — **Phone Number** — §164.312(a)(1)
  - PHI field 'PHONE' found in code without protection
  - Code: `Violation: Phone Number`

- [ ] `test_patient-api_app_py.py:1019` — **Email Address** — §164.312(a)(1)
  - PHI field 'EMAIL' found in code without protection
  - Code: `Violation: Email Address`

- [ ] `test_patient-api_app_py.py:1123` — **Phone Number** — §164.312(a)(1)
  - PHI field 'PHONE' found in code without protection
  - Code: `Violation: Phone Number`

- [ ] `test_patient-api_app_py.py:1175` — **Email Address** — §164.312(a)(1)
  - PHI field 'EMAIL' found in code without protection
  - Code: `Violation: Email Address`

- [ ] `test_patient-api_app_py.py:1279` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `Violation: Diagnosis / ICD Code`

- [ ] `test_patient-api_app_py.py:1383` — **Email Address** — §164.312(a)(1)
  - PHI field 'EMAIL' found in code without protection
  - Code: `Violation: Email Address`

- [ ] `test_patient-api_app_py.py:1695` — **Phone Number** — §164.312(a)(1)
  - PHI field 'PHONE' found in code without protection
  - Code: `Violation: Phone Number`

- [ ] `test_patient-api_app_py.py:1747` — **Email Address** — §164.312(a)(1)
  - PHI field 'EMAIL' found in code without protection
  - Code: `Violation: Email Address`

- [ ] `test_patient-api_app_py.py:1851` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `Violation: Diagnosis / ICD Code`

- [ ] `test_patient-api_app_py.py:1955` — **Phone Number** — §164.312(a)(1)
  - PHI field 'PHONE' found in code without protection
  - Code: `Violation: Phone Number`

- [ ] `test_patient-api_app_py.py:2007` — **Email Address** — §164.312(a)(1)
  - PHI field 'EMAIL' found in code without protection
  - Code: `Violation: Email Address`

- [ ] `test_patient-api_app_py.py:2111` — **Diagnosis / ICD Code** — §164.502(b)
  - PHI field 'DIAGNOSIS' found in code without protection
  - Code: `Violation: Diagnosis / ICD Code`

### Medium (41)

- [ ] `audit-logger\app.py:46` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `"ip_address": request.remote_addr          # IP is PHI under HIPAA`

- [ ] `audit-logger\app.py:55` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `f"Action: {event['action']} | IP: {event['ip_address']}")`

- [ ] `audit-logger\app.py:101` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `app.run(host="0.0.0.0", port=5003, debug=True)`

- [ ] `audit-logger\config.py:32` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `HOST = "0.0.0.0"`

- [ ] `audit-logger\tests\test_integration.py:94` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `assert 'ip_address' in event, "IP address is stored (HIPAA identifier)"`

- [ ] `audit-logger\tests\test_integration.py:94` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `assert 'ip_address' in event, "IP address is stored (HIPAA identifier)"`

- [ ] `audit-logger\tests\test_integration.py:95` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `assert event['ip_address'] is not None`

- [ ] `audit_events.log:2` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `* Running on all addresses (0.0.0.0)`

- [ ] `audit_events.log:3` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `* Running on http://127.0.0.1:5003`

- [ ] `audit_events.log:4` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `* Running on http://10.161.218.8:5003`

- [ ] `billing-service\app.py:109` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `app.run(host="0.0.0.0", port=5002, debug=True)`

- [ ] `billing-service\config.py:23` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `HOST = "0.0.0.0"`

- [ ] `patient-api\app.py:40` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `address TEXT`

- [ ] `patient-api\app.py:46` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `INSERT OR IGNORE INTO patients (id, full_name, ssn, date_of_birth, medical_record_number, diagnosis,`

- [ ] `patient-api\app.py:47` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `VALUES (1, 'John Smith', '123-45-6789', '1985-03-15', 'MRN-001234', 'Type 2 Diabetes', '555-0123', '`

- [ ] `patient-api\app.py:85` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `"INSERT INTO patients (full_name, ssn, date_of_birth, medical_record_number, diagnosis, phone_number`

- [ ] `patient-api\app.py:86` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `(data["full_name"], data["ssn"], data["date_of_birth"], data["medical_record_number"], data["diagnos`

- [ ] `patient-api\app.py:99` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `app.run(host="0.0.0.0", port=5001, debug=True)`

- [ ] `patient-api\config.py:18` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `HOST = "0.0.0.0"`

- [ ] `patient-api\tests\test_integration.py:33` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `"address": "456 Test Ave"`

- [ ] `patient-api\tests\test_patient_api.py:64` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `assert 'address' in data`

- [ ] `patient-api\tests\test_patient_api.py:78` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `"address": "123 Test St"`

- [ ] `shared\phi_utils.py:74` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `'address', 'street', 'city', 'zip', 'zipcode',`

- [ ] `shared\phi_utils.py:76` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `'ip_address', 'ip'`

- [ ] `shared\test_data.py:49` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `"""Generate a fake address"""`

- [ ] `shared\test_data.py:70` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `"address": generate_address()`

- [ ] `test_audit-logger_app_py.py:863` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: IP Address`

- [ ] `test_audit-logger_app_py.py:915` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: IP Address`

- [ ] `test_audit-logger_app_py.py:967` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: IP Address`

- [ ] `test_billing-service_app_py.py:707` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: IP Address`

- [ ] `test_patient-api_app_py.py:1019` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: Email Address`

- [ ] `test_patient-api_app_py.py:1175` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: Email Address`

- [ ] `test_patient-api_app_py.py:1383` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: Email Address`

- [ ] `test_patient-api_app_py.py:1747` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: Email Address`

- [ ] `test_patient-api_app_py.py:2007` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: Email Address`

- [ ] `test_patient-api_app_py.py:2215` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: Street Address`

- [ ] `test_patient-api_app_py.py:2267` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: Street Address`

- [ ] `test_patient-api_app_py.py:2319` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: Street Address`

- [ ] `test_patient-api_app_py.py:2371` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: Street Address`

- [ ] `test_patient-api_app_py.py:2423` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: Street Address`

- [ ] `test_patient-api_app_py.py:2475` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `Violation: IP Address`

---

## PHI Flow Map

| Service | PHI Types Accessed |
|---------|-------------------|
| `root` | ADDRESS, DIAGNOSIS, DOB, EMAIL, IP, PHONE, SSN |
| `audit-logger` | ADDRESS, IP, MRN, NAME, SSN |
| `billing-service` | DIAGNOSIS, DOB, IP, MRN, NAME, SSN |
| `patient-api` | ADDRESS, DIAGNOSIS, DOB, EMAIL, IP, MRN, NAME, PHONE, SSN |
| `shared` | ADDRESS, DIAGNOSIS, DOB, EMAIL, IP, MRN, NAME, PHONE, SSN |

---

## Compliance Checklist

- [ ] All Critical violations resolved
- [ ] All High violations resolved
- [ ] Encryption at rest implemented (AES-256)
- [ ] TLS 1.2+ enforced for all PHI transmission
- [ ] Authentication on all PHI endpoints
- [ ] PHI redacted in all log outputs
- [ ] Audit trail implemented
- [ ] All compliance tests passing

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Compliance Officer | | | |
| Engineering Lead | | | |
| Security Architect | | | |

---

*Generated by IBM Bob PHI Compliance Scanner*