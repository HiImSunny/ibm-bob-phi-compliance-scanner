# PHI Utility Functions
# WARNING: Contains intentional HIPAA violations for demo purposes

import re

# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation: Weak PHI masking function with predictable pattern
# HIPAA Rule: §164.514(b)(2) - De-identification standard
# Severity: Medium
# Issue: Masking pattern is predictable and reversible
# Last 4 digits of SSN can be used to re-identify individuals when combined with other data
def mask_ssn_weak(ssn):
    """
    Weakly mask SSN by showing last 4 digits.
    VIOLATION: This is not sufficient de-identification per HIPAA Safe Harbor method.
    """
    if not ssn or len(ssn) < 4:
        return "***-**-****"
    return f"***-**-{ssn[-4:]}"


def mask_name_weak(full_name):
    """
    Weakly mask name by showing first name and last initial.
    VIOLATION: First name + initial is often enough to re-identify.
    """
    if not full_name:
        return "***"
    parts = full_name.split()
    if len(parts) == 1:
        return f"{parts[0][0]}***"
    return f"{parts[0]} {parts[-1][0]}***"


def mask_mrn_weak(mrn):
    """
    Weakly mask MRN by showing last 3 digits.
    VIOLATION: MRNs are unique identifiers and should be fully redacted or tokenized.
    """
    if not mrn or len(mrn) < 3:
        return "MRN-***"
    return f"MRN-***{mrn[-3:]}"


# INTENTIONAL HIPAA VIOLATION FOR DEMO
# Violation: Validation function that logs PHI when validation fails
# HIPAA Rule: §164.312(b) - Audit controls
# Severity: High
def validate_ssn(ssn):
    """
    Validate SSN format.
    VIOLATION: Logs invalid SSN attempts with actual SSN value.
    """
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    if not re.match(pattern, ssn):
        # VIOLATION: Logging the actual SSN value
        print(f"[VALIDATION ERROR] Invalid SSN format: {ssn}")
        return False
    return True


def is_phi_field(field_name):
    """
    Check if a field name indicates PHI content.
    Used by scanners to identify potential violations.
    """
    phi_indicators = [
        'ssn', 'social_security', 'social_security_number',
        'name', 'full_name', 'first_name', 'last_name',
        'dob', 'date_of_birth', 'birth_date',
        'mrn', 'medical_record', 'medical_record_number',
        'phone', 'phone_number', 'telephone',
        'email', 'email_address',
        'address', 'street', 'city', 'zip', 'zipcode',
        'diagnosis', 'condition', 'procedure',
        'ip_address', 'ip'
    ]
    field_lower = field_name.lower()
    return any(indicator in field_lower for indicator in phi_indicators)

# Made with Bob
