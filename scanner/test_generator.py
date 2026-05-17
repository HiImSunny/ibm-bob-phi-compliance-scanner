# test_generator.py
# Auto-generates pytest test stubs for patched PHI functions

import json
import os
import re
from pathlib import Path
from datetime import datetime


# ── Filtering Configuration ──────────────────────────────────────────────────

SKIP_FILE_PATTERNS = [
    r'\.md$',           # Documentation
    r'\.txt$',          # Text files
    r'\.log$',          # Log files
    r'test_.*\.py$',    # Test files
    r'.*_test\.py$',    # Test files
    r'README',          # README files
]

def should_generate_test(violation: dict) -> bool:
    """Determine if violation needs a test"""
    # Skip non-code files
    for pattern in SKIP_FILE_PATTERNS:
        if re.search(pattern, violation["file"]):
            return False
    
    # Only generate for Critical/High severity
    if violation["severity"] not in ("Critical", "High"):
        return False
    
    # Only generate for Python files
    if not violation["file"].endswith(".py"):
        return False
    
    return True


# ── Violation-Specific Test Templates ────────────────────────────────────────

LOG_PHI_TEST_TEMPLATE = '''
    def test_log_redaction_line_{line_no}(self, caplog):
        """
        {hipaa_rule} — PHI must be redacted in logs
        Violation at {source_file}:{line_no}
        """
        import logging
        with caplog.at_level(logging.INFO):
            # TODO: Trigger the function that logs PHI
            # Example: client.get('/endpoint')
            pass
        
        # Verify no PHI in any log record
        for record in caplog.records:
            assert not contains_phi(record.message), (
                f"Raw PHI found in log: {{record.message}}"
            )
'''

MISSING_AUTH_TEST_TEMPLATE = '''
    def test_auth_required_line_{line_no}(self, client):
        """
        {hipaa_rule} — Endpoint must require authentication
        Violation at {source_file}:{line_no}
        """
        # Make unauthenticated request
        response = client.get('{endpoint_path}')
        
        # Should return 401 Unauthorized or 403 Forbidden
        assert response.status_code in (401, 403), (
            f"Expected 401/403 for unauthenticated request, got {{response.status_code}}"
        )
'''

HTTP_TRANSMISSION_TEST_TEMPLATE = '''
    def test_https_enforced_line_{line_no}(self):
        """
        {hipaa_rule} — PHI must be transmitted over HTTPS
        Violation at {source_file}:{line_no}
        """
        # Verify code uses HTTPS, not HTTP
        code_snippet = "{snippet}"
        assert 'http://' not in code_snippet.lower() or 'localhost' in code_snippet.lower(), (
            "HTTP transmission detected — must use HTTPS for PHI"
        )
'''

PHI_EXPOSURE_TEST_TEMPLATE = '''
    def test_phi_redacted_line_{line_no}(self, client):
        """
        {hipaa_rule} — PHI must be redacted in responses
        Violation at {source_file}:{line_no}
        """
        # TODO: Make request that returns PHI
        response = client.get('/endpoint')
        data = response.get_json() if response.content_type == 'application/json' else response.data
        
        # Verify no raw PHI in response
        assert not contains_phi(str(data)), (
            "Raw PHI found in response — must be redacted or encrypted"
        )
'''

TEMPLATE_MAP = {
    "LOG_PHI": LOG_PHI_TEST_TEMPLATE,
    "MISSING_AUTH": MISSING_AUTH_TEST_TEMPLATE,
    "HTTP_TRANSMISSION": HTTP_TRANSMISSION_TEST_TEMPLATE,
    "SSN": PHI_EXPOSURE_TEST_TEMPLATE,
    "MRN": PHI_EXPOSURE_TEST_TEMPLATE,
    "DOB": PHI_EXPOSURE_TEST_TEMPLATE,
    "PHONE": PHI_EXPOSURE_TEST_TEMPLATE,
    "EMAIL": PHI_EXPOSURE_TEST_TEMPLATE,
}


# ── Service-Specific Fixtures ─────────────────────────────────────────────────

def generate_fixtures(source_file: str) -> str:
    """Generate pytest fixtures based on source file"""
    
    if "patient-api" in source_file:
        return '''
@pytest.fixture
def client():
    """Flask test client for patient-api"""
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ehr-demo/patient-api')))
    from app import app, init_db
    app.config['TESTING'] = True
    app.config['DATABASE'] = ':memory:'
    init_db()
    with app.test_client() as client:
        yield client
'''
    
    elif "audit-logger" in source_file:
        return '''
@pytest.fixture
def client():
    """Flask test client for audit-logger"""
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ehr-demo/audit-logger')))
    from app import app, audit_events
    app.config['TESTING'] = True
    audit_events.clear()
    with app.test_client() as client:
        yield client
'''
    
    elif "billing-service" in source_file:
        return '''
@pytest.fixture
def client():
    """Flask test client for billing-service"""
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ehr-demo/billing-service')))
    from app import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
'''
    
    return ""  # No fixtures for other files


def extract_endpoint_path(snippet: str) -> str:
    """Extract endpoint path from Flask route decorator"""
    match = re.search(r'@app\.route\(["\']([^"\']+)["\']', snippet)
    return match.group(1) if match else "/"


# ── Test File Template ────────────────────────────────────────────────────────

TEST_TEMPLATE = '''# Auto-generated by IBM Bob PHI Compliance Scanner
# Generated: {timestamp}
# Source: {source_file}
# HIPAA Rules covered: {hipaa_rules}

import pytest
import re

{fixtures}

# ── Helpers ──────────────────────────────────────────────────────────────────

SSN_PATTERN    = re.compile(r'\\b\\d{{3}}-\\d{{2}}-\\d{{4}}\\b')
MRN_PATTERN    = re.compile(r'\\bMRN-?\\d{{4,}}\\b', re.IGNORECASE)
EMAIL_PATTERN  = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{{2,}}')
PHONE_PATTERN  = re.compile(r'\\b\\d{{3}}[-.]\\d{{3}}[-.]\\d{{4}}\\b')

def contains_phi(text: str) -> bool:
    """Returns True if text contains any raw PHI."""
    t = str(text)
    return bool(
        SSN_PATTERN.search(t) or
        MRN_PATTERN.search(t) or
        EMAIL_PATTERN.search(t) or
        PHONE_PATTERN.search(t)
    )

# ── Tests ─────────────────────────────────────────────────────────────────────

class Test{class_name}:
    """
    PHI Compliance tests for {source_file}
    Generated from scanner violations
    """
{test_cases}
'''


def generate_tests(violations_json_path: str, output_dir: str):
    """
    Read violations JSON from scanner output and generate pytest files.
    """
    with open(violations_json_path) as f:
        data = json.load(f)

    violations = data.get("violations", [])
    if not violations:
        print("[TestGen] No violations found — nothing to generate.")
        return

    # Group violations by source file
    by_file: dict[str, list] = {}
    for v in violations:
        by_file.setdefault(v["file"], []).append(v)

    # Create generated_tests directory
    gen_tests_dir = Path(output_dir) / "generated_tests"
    gen_tests_dir.mkdir(parents=True, exist_ok=True)
    
    # Create __init__.py for package
    (gen_tests_dir / "__init__.py").write_text("# Generated tests package\n")
    
    generated = []

    for source_file, viols in by_file.items():
        # Filter violations that should have tests
        testable_viols = [v for v in viols if should_generate_test(v)]
        
        if not testable_viols:
            continue  # Skip files with no testable violations
        
        # Build test cases for this file
        test_cases = []
        hipaa_rules = sorted({v["hipaa_rule"] for v in testable_viols})
        
        for v in testable_viols:
            # Get appropriate template
            template = TEMPLATE_MAP.get(v["phi_type"], PHI_EXPOSURE_TEST_TEMPLATE)
            
            # Extract endpoint path for auth tests
            endpoint_path = extract_endpoint_path(v["snippet"]) if v["phi_type"] == "MISSING_AUTH" else "/"
            
            class_name = (
                v["phi_type"].replace("-", "").replace("_", "").title() +
                f"Line{v['line']}"
            )
            
            test_cases.append(template.format(
                class_name=class_name,
                source_file=source_file,
                line_no=v["line"],
                phi_name=v["phi_name"],
                hipaa_rule=v["hipaa_rule"],
                snippet=v["snippet"].replace('"', '\\"')[:100],  # Escape quotes and limit length
                endpoint_path=endpoint_path,
            ))
        
        if not test_cases:
            continue  # Skip if no tests generated

        # Derive test filename
        safe_name = source_file.replace("/", "_").replace("\\", "_").replace(".", "_")
        test_filename = f"test_{safe_name}.py"
        test_path = Path(output_dir) / "generated_tests" / test_filename

        # Generate fixtures for this service
        fixtures = generate_fixtures(source_file)
        
        # Create a safe class name from the source file
        safe_class_name = source_file.replace("/", "_").replace("\\", "_").replace(".", "_").replace("-", "_").title()

        content = TEST_TEMPLATE.format(
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            source_file=source_file,
            hipaa_rules=", ".join(hipaa_rules),
            fixtures=fixtures,
            class_name=safe_class_name,
            test_cases="\n".join(test_cases),
        )

        test_path.write_text(content, encoding="utf-8")
        generated.append(str(test_path))
        print(f"[TestGen] Generated: {test_path}")

    print(f"\n[TestGen] {len(generated)} test file(s) created in: {output_dir}")
    return generated


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate pytest stubs from PHI scan results")
    parser.add_argument("--violations", required=True, help="Path to violations JSON file")
    parser.add_argument("--output", default="../ehr-demo", help="Output directory for test files")
    args = parser.parse_args()
    generate_tests(args.violations, args.output)
