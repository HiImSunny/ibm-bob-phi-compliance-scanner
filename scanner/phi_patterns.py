# phi_patterns.py
# HIPAA 18 PHI identifier regex patterns

import re

PHI_PATTERNS = [
    {
        "id": "SSN",
        "name": "Social Security Number",
        "hipaa_rule": "§164.312(a)(1)",
        "severity": "Critical",
        "pattern": re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
        "var_names": re.compile(
            r'\b(ssn|social_security|social_security_number|sin)\b',
            re.IGNORECASE
        ),
    },
    {
        "id": "MRN",
        "name": "Medical Record Number",
        "hipaa_rule": "§164.312(a)(1)",
        "severity": "Critical",
        "pattern": re.compile(r'\bMRN-?\d{4,}\b', re.IGNORECASE),
        "var_names": re.compile(
            r'\b(mrn|medical_record_number|medical_record|record_number)\b',
            re.IGNORECASE
        ),
    },
    {
        "id": "DOB",
        "name": "Date of Birth",
        "hipaa_rule": "§164.312(a)(1)",
        "severity": "High",
        "pattern": re.compile(
            r'\b(19|20)\d{2}[-/](0[1-9]|1[0-2])[-/](0[1-9]|[12]\d|3[01])\b'
        ),
        "var_names": re.compile(
            r'\b(dob|date_of_birth|birth_date|birthdate|birthday)\b',
            re.IGNORECASE
        ),
    },
    {
        "id": "PHONE",
        "name": "Phone Number",
        "hipaa_rule": "§164.312(a)(1)",
        "severity": "High",
        "pattern": re.compile(r'\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b'),
        "var_names": re.compile(
            r'\b(phone|phone_number|fax|fax_number|mobile|cell)\b',
            re.IGNORECASE
        ),
    },
    {
        "id": "EMAIL",
        "name": "Email Address",
        "hipaa_rule": "§164.312(a)(1)",
        "severity": "High",
        "pattern": re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
        "var_names": re.compile(
            r'\b(email|email_address|e_mail)\b',
            re.IGNORECASE
        ),
    },
    {
        "id": "NAME",
        "name": "Patient Name",
        "hipaa_rule": "§164.312(a)(1)",
        "severity": "High",
        "pattern": None,  # detected via var_names only
        "var_names": re.compile(
            r'\b(patient_name|full_name|first_name|last_name|patient_full_name)\b',
            re.IGNORECASE
        ),
    },
    {
        "id": "ADDRESS",
        "name": "Street Address",
        "hipaa_rule": "§164.312(a)(1)",
        "severity": "Medium",
        "pattern": re.compile(r'\b\d+\s+\w+\s+(St|Ave|Blvd|Rd|Dr|Ln|Way|Ct)\b', re.IGNORECASE),
        "var_names": re.compile(
            r'\b(address|street_address|home_address|mailing_address)\b',
            re.IGNORECASE
        ),
    },
    {
        "id": "IP",
        "name": "IP Address",
        "hipaa_rule": "§164.312(e)(1)",
        "severity": "Medium",
        "pattern": re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b'),
        "var_names": re.compile(
            r'\b(ip_address|remote_addr|client_ip|user_ip)\b',
            re.IGNORECASE
        ),
    },
    {
        "id": "DIAGNOSIS",
        "name": "Diagnosis / ICD Code",
        "hipaa_rule": "§164.502(b)",
        "severity": "High",
        "pattern": re.compile(r'\b[A-Z]\d{2}\.?\d{0,2}\b'),  # ICD-10 pattern
        "var_names": re.compile(
            r'\b(diagnosis|diagnosis_code|icd_code|condition|medical_condition)\b',
            re.IGNORECASE
        ),
    },
]

# Patterns for detecting PHI in log statements
LOG_PATTERNS = re.compile(
    r'(logger\.|logging\.|print\(|console\.log\()',
    re.IGNORECASE
)

# Patterns for detecting unprotected PHI endpoints
ENDPOINT_PATTERNS = re.compile(
    r'@app\.route\s*\(.*\)\s*\ndef\s+\w+',
    re.DOTALL
)

# Patterns for HTTP (not HTTPS) usage
HTTP_PATTERN = re.compile(r'http://(?!localhost|127\.0\.0\.1)', re.IGNORECASE)

# Patterns for unencrypted file writes
FILE_WRITE_PATTERN = re.compile(
    r'open\s*\([^)]+["\']w["\']',
    re.IGNORECASE
)
