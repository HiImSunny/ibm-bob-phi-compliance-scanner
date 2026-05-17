# test_scanner_output.py
# Tests to verify scanner itself works correctly

import pytest
import json
import sys
import os
from pathlib import Path

# Add scanner directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from phi_scanner import PHIScanner
from phi_patterns import PHI_PATTERNS


class TestScannerOutput:
    """Verify scanner produces expected output"""
    
    def test_scanner_detects_violations(self):
        """Scanner should detect violations in ehr-demo"""
        scanner = PHIScanner("../../ehr-demo")
        violations = scanner.scan()
        
        assert len(violations) > 0, "Scanner should detect violations"
        assert len(violations) > 50, f"Expected >50 violations, got {len(violations)}"
    
    def test_scanner_detects_log_phi(self):
        """Scanner should detect LOG_PHI violations"""
        scanner = PHIScanner("../../ehr-demo")
        violations = scanner.scan()
        
        log_phi = [v for v in violations if v.phi_type == "LOG_PHI"]
        assert len(log_phi) > 0, "Should detect LOG_PHI violations"
    
    def test_scanner_detects_missing_auth(self):
        """Scanner should detect MISSING_AUTH violations"""
        scanner = PHIScanner("../../ehr-demo")
        violations = scanner.scan()
        
        missing_auth = [v for v in violations if v.phi_type == "MISSING_AUTH"]
        assert len(missing_auth) > 0, "Should detect MISSING_AUTH violations"
    
    def test_scanner_detects_ssn_violations(self):
        """Scanner should detect SSN violations"""
        scanner = PHIScanner("../../ehr-demo")
        violations = scanner.scan()
        
        ssn_viols = [v for v in violations if v.phi_type == "SSN"]
        assert len(ssn_viols) > 0, "Should detect SSN violations"
    
    def test_json_export_valid(self, tmp_path):
        """JSON export should be valid JSON"""
        scanner = PHIScanner("../../ehr-demo")
        scanner.scan()
        
        json_path = tmp_path / "test_report.json"
        scanner.export_json(str(json_path))
        
        # Verify file exists and is valid JSON
        assert json_path.exists()
        with open(json_path) as f:
            data = json.load(f)
        
        assert "violations" in data
        assert "phi_flow" in data
        assert data["total_violations"] > 0
    
    def test_markdown_export_valid(self, tmp_path):
        """Markdown export should be valid"""
        scanner = PHIScanner("../../ehr-demo")
        scanner.scan()
        
        md_path = tmp_path / "test_report.md"
        scanner.export_markdown(str(md_path))
        
        # Verify file exists and contains expected sections
        assert md_path.exists()
        content = md_path.read_text()
        
        assert "# HIPAA PHI Compliance Audit Report" in content
        assert "## Violations by Severity" in content
        assert "## PHI Flow Map" in content
    
    def test_phi_flow_mapping(self):
        """PHI flow map should track service-level PHI access"""
        scanner = PHIScanner("../../ehr-demo")
        scanner.scan()
        
        assert len(scanner.phi_flow) > 0, "Should track PHI flow"
        # Check that at least one service is tracked
        assert any("patient" in str(k).lower() or "audit" in str(k).lower() 
                   for k in scanner.phi_flow.keys()), "Should track patient-api or audit-logger"
    
    def test_severity_classification(self):
        """Violations should be properly classified by severity"""
        scanner = PHIScanner("../../ehr-demo")
        violations = scanner.scan()
        
        severities = {v.severity for v in violations}
        assert "Critical" in severities or "High" in severities, "Should have Critical or High severity violations"
    
    def test_hipaa_rule_references(self):
        """All violations should reference HIPAA rules"""
        scanner = PHIScanner("../../ehr-demo")
        violations = scanner.scan()
        
        for v in violations:
            assert v.hipaa_rule, f"Violation at {v.file_path}:{v.line_no} missing HIPAA rule"
            assert "§164" in v.hipaa_rule, f"HIPAA rule should reference §164: {v.hipaa_rule}"


class TestPHIPatterns:
    """Test PHI pattern detection"""
    
    def test_ssn_pattern_matches(self):
        """SSN pattern should match valid SSNs"""
        from phi_patterns import PHI_PATTERNS
        
        ssn_pattern = next(p for p in PHI_PATTERNS if p["id"] == "SSN")
        
        # Should match
        assert ssn_pattern["pattern"].search("123-45-6789")
        assert ssn_pattern["var_names"].search("ssn")  # Match just 'ssn' not 'patient_ssn'
        assert ssn_pattern["var_names"].search("social_security_number")
        
        # Should not match
        assert not ssn_pattern["pattern"].search("12-345-6789")
    
    def test_mrn_pattern_matches(self):
        """MRN pattern should match valid MRNs"""
        from phi_patterns import PHI_PATTERNS
        
        mrn_pattern = next(p for p in PHI_PATTERNS if p["id"] == "MRN")
        
        # Should match
        assert mrn_pattern["pattern"].search("MRN-001234")
        assert mrn_pattern["var_names"].search("medical_record_number")
    
    def test_log_pattern_detection(self):
        """Log patterns should detect logging statements"""
        from phi_patterns import LOG_PATTERNS
        
        assert LOG_PATTERNS.search("logger.info('test')")
        assert LOG_PATTERNS.search("logging.debug('test')")
        assert LOG_PATTERNS.search("print('test')")
        assert LOG_PATTERNS.search("console.log('test')")

# Made with Bob
