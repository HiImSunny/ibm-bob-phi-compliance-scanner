# HIPAA PHI Compliance Audit Report

**Generated**: 2026-05-17 20:08:25  
**Repository**: `D:\Code Project\Python Coding\IBM Bob Hackathon\ehr-demo`  
**Scanned files**: 16  
**Violations found**: 119  

---

## Executive Summary

Automated PHI scan identified **119 violations** across 16 files: 48 Critical, 53 High, 18 Medium. Immediate remediation required for Critical violations before next deployment. All violations must be resolved to achieve HIPAA compliance.

---

## Violations by Severity

### Critical (48)

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

### High (53)

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

### Medium (18)

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

- [ ] `shared\phi_utils.py:74` — **Street Address** — §164.312(a)(1)
  - PHI field 'ADDRESS' found in code without protection
  - Code: `'address', 'street', 'city', 'zip', 'zipcode',`

- [ ] `shared\phi_utils.py:76` — **IP Address** — §164.312(e)(1)
  - PHI field 'IP' found in code without protection
  - Code: `'ip_address', 'ip'`

---

## PHI Flow Map

| Service | PHI Types Accessed |
|---------|-------------------|
| `root` | DOB, IP |
| `audit-logger` | IP, MRN, NAME, SSN |
| `billing-service` | DIAGNOSIS, DOB, IP, NAME, SSN |
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