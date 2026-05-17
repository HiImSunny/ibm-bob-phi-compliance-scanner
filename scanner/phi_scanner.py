# phi_scanner.py
# Main PHI compliance scanner engine
# Usage: python phi_scanner.py --repo ../ehr-demo --output ../reports/audit-report.md

import os
import re
import json
import argparse
from datetime import datetime
from pathlib import Path
from phi_patterns import (
    PHI_PATTERNS, LOG_PATTERNS, HTTP_PATTERN, FILE_WRITE_PATTERN
)

SCANNABLE_EXTENSIONS = {".py", ".js", ".ts", ".java", ".sql", ".json",
                         ".yaml", ".yml", ".env", ".txt", ".md", ".log"}

# Skip patterns for demo reliability - exclude test files and documentation
SKIP_FILE_PATTERNS = [
    r'test_.*\.py$',        # Test files
    r'.*_test\.py$',        # Test files
    r'/tests/',             # Test directories
    r'README\.md$',         # README files
    r'PLAN.*\.md$',         # Planning docs
    r'PRD.*\.md$',          # Product docs
    r'slides.*\.md$',       # Slide content
    r'bob_sessions/',       # Bob session logs
]

SEVERITY_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}


class Violation:
    def __init__(self, file_path, line_no, col, phi_type, phi_name,
                 hipaa_rule, severity, snippet, context):
        self.file_path = file_path
        self.line_no = line_no
        self.col = col
        self.phi_type = phi_type
        self.phi_name = phi_name
        self.hipaa_rule = hipaa_rule
        self.severity = severity
        self.snippet = snippet.strip()
        self.context = context

    def to_dict(self):
        return {
            "file": self.file_path,
            "line": self.line_no,
            "col": self.col,
            "phi_type": self.phi_type,
            "phi_name": self.phi_name,
            "hipaa_rule": self.hipaa_rule,
            "severity": self.severity,
            "snippet": self.snippet,
        }


class PHIScanner:
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path).resolve()
        self.violations: list[Violation] = []
        self.scanned_files: list[str] = []
        self.phi_flow: dict = {}  # service -> list of PHI types touched

    def scan(self):
        print(f"\n[PHI Scanner] Scanning: {self.repo_path}")
        print(f"[PHI Scanner] Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        for root, dirs, files in os.walk(self.repo_path):
            # Skip hidden dirs and virtual envs
            dirs[:] = [d for d in dirs if not d.startswith(".")
                       and d not in ("__pycache__", "node_modules", "venv", ".venv")]
            for fname in files:
                fpath = Path(root) / fname
                if fpath.suffix.lower() in SCANNABLE_EXTENSIONS:
                    self._scan_file(fpath)

        self.violations.sort(key=lambda v: (SEVERITY_ORDER.get(v.severity, 9), v.file_path, v.line_no))
        print(f"\n[PHI Scanner] Scanned {len(self.scanned_files)} files")
        print(f"[PHI Scanner] Found {len(self.violations)} violations\n")
        return self.violations

    def _scan_file(self, fpath: Path):
        rel_path = str(fpath.relative_to(self.repo_path))
        
        # Skip files matching exclusion patterns
        for pattern in SKIP_FILE_PATTERNS:
            if re.search(pattern, rel_path):
                return
        
        try:
            content = fpath.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            return

        self.scanned_files.append(rel_path)
        lines = content.splitlines()
        service = rel_path.split(os.sep)[0] if os.sep in rel_path else "root"

        for line_no, line in enumerate(lines, start=1):
            self._check_phi_patterns(rel_path, line_no, line, service)
            self._check_log_with_phi(rel_path, line_no, line, lines, service)
            self._check_http(rel_path, line_no, line, service)
            self._check_file_write(rel_path, line_no, line, lines, service)

        # Check for missing auth decorators on routes
        self._check_missing_auth(rel_path, content, service)

    def _check_phi_patterns(self, rel_path, line_no, line, service):
        for phi in PHI_PATTERNS:
            matched = False

            # Check variable name patterns
            if phi["var_names"] and phi["var_names"].search(line):
                matched = True

            # Check value patterns (e.g. actual SSN format)
            if not matched and phi["pattern"] and phi["pattern"].search(line):
                matched = True

            if matched:
                # Skip comment lines
                stripped = line.strip()
                if stripped.startswith("#") or stripped.startswith("//"):
                    continue

                self._add_violation(
                    file_path=rel_path,
                    line_no=line_no,
                    col=0,
                    phi_type=phi["id"],
                    phi_name=phi["name"],
                    hipaa_rule=phi["hipaa_rule"],
                    severity=phi["severity"],
                    snippet=line,
                    context=f"PHI field '{phi['id']}' found in code without protection"
                )
                # Track PHI flow
                if service not in self.phi_flow:
                    self.phi_flow[service] = set()
                self.phi_flow[service].add(phi["id"])

    def _check_log_with_phi(self, rel_path, line_no, line, lines, service):
        if not LOG_PATTERNS.search(line):
            return
        for phi in PHI_PATTERNS:
            if phi["var_names"] and phi["var_names"].search(line):
                self._add_violation(
                    file_path=rel_path,
                    line_no=line_no,
                    col=0,
                    phi_type="LOG_PHI",
                    phi_name=f"PHI in log: {phi['name']}",
                    hipaa_rule="§164.312(b)",
                    severity="Critical",
                    snippet=line,
                    context=f"Raw {phi['name']} written to log output — must be redacted"
                )

    def _check_http(self, rel_path, line_no, line, service):
        if HTTP_PATTERN.search(line):
            stripped = line.strip()
            if stripped.startswith("#") or stripped.startswith("//"):
                return
            self._add_violation(
                file_path=rel_path,
                line_no=line_no,
                col=0,
                phi_type="HTTP_TRANSMISSION",
                phi_name="Unencrypted HTTP transmission",
                hipaa_rule="§164.312(e)(1)",
                severity="Critical",
                snippet=line,
                context="PHI transmitted over HTTP — must use HTTPS (TLS 1.2+)"
            )

    def _check_file_write(self, rel_path, line_no, line, lines, service):
        if FILE_WRITE_PATTERN.search(line):
            # Check surrounding lines for PHI variable names
            context_window = lines[max(0, line_no - 5):line_no + 5]
            context_text = " ".join(context_window)
            for phi in PHI_PATTERNS:
                if phi["var_names"] and phi["var_names"].search(context_text):
                    self._add_violation(
                        file_path=rel_path,
                        line_no=line_no,
                        col=0,
                        phi_type="UNENCRYPTED_FILE",
                        phi_name="PHI written to unencrypted file",
                        hipaa_rule="§164.312(a)(1)",
                        severity="High",
                        snippet=line,
                        context=f"File write near PHI field '{phi['id']}' — must encrypt before writing"
                    )
                    break

    def _check_missing_auth(self, rel_path, content, service):
        # Find Flask routes without auth decorators
        route_pattern = re.compile(
            r'(@app\.route\([^)]+\))\s*\n(?!\s*@require_auth)(?!\s*@login_required)'
            r'(?!\s*@jwt_required)',
            re.MULTILINE
        )
        for match in route_pattern.finditer(content):
            line_no = content[:match.start()].count("\n") + 1
            self._add_violation(
                file_path=rel_path,
                line_no=line_no,
                col=0,
                phi_type="MISSING_AUTH",
                phi_name="Endpoint missing authentication",
                hipaa_rule="§164.312(d)",
                severity="High",
                snippet=match.group(0).strip(),
                context="API endpoint has no authentication decorator — PHI accessible without credentials"
            )

    def _add_violation(self, **kwargs):
        # Deduplicate: same file + line + phi_type
        key = (kwargs["file_path"], kwargs["line_no"], kwargs["phi_type"])
        existing = {(v.file_path, v.line_no, v.phi_type) for v in self.violations}
        if key not in existing:
            self.violations.append(Violation(**kwargs))

    def print_report(self):
        by_severity = {}
        for v in self.violations:
            by_severity.setdefault(v.severity, []).append(v)

        print("=" * 70)
        print("  PHI COMPLIANCE SCAN RESULTS")
        print("=" * 70)
        print(f"  Repository : {self.repo_path}")
        print(f"  Scanned    : {len(self.scanned_files)} files")
        print(f"  Violations : {len(self.violations)} total")
        print()

        for sev in ["Critical", "High", "Medium", "Low"]:
            items = by_severity.get(sev, [])
            if not items:
                continue
            print(f"  [{sev.upper()}] — {len(items)} violation(s)")
            print("-" * 70)
            for v in items:
                print(f"  {v.file_path}:{v.line_no}")
                print(f"    Type    : {v.phi_name}")
                print(f"    Rule    : {v.hipaa_rule}")
                print(f"    Context : {v.context}")
                print(f"    Code    : {v.snippet[:80]}{'...' if len(v.snippet) > 80 else ''}")
                print()

        print("=" * 70)
        print("  PHI FLOW MAP")
        print("=" * 70)
        for service, phi_types in self.phi_flow.items():
            print(f"  {service:30s} touches: {', '.join(sorted(phi_types))}")
        print()

    def export_json(self, output_path: str):
        data = {
            "scan_timestamp": datetime.now().isoformat(),
            "repository": str(self.repo_path),
            "scanned_files": len(self.scanned_files),
            "total_violations": len(self.violations),
            "phi_flow": {k: list(v) for k, v in self.phi_flow.items()},
            "violations": [v.to_dict() for v in self.violations],
        }
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"[PHI Scanner] JSON report saved: {output_path}")

    def export_markdown(self, output_path: str):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        by_severity = {}
        for v in self.violations:
            by_severity.setdefault(v.severity, []).append(v)

        lines = [
            "# HIPAA PHI Compliance Audit Report",
            "",
            f"**Generated**: {now}  ",
            f"**Repository**: `{self.repo_path}`  ",
            f"**Scanned files**: {len(self.scanned_files)}  ",
            f"**Violations found**: {len(self.violations)}  ",
            "",
            "---",
            "",
            "## Executive Summary",
            "",
        ]

        critical = len(by_severity.get("Critical", []))
        high = len(by_severity.get("High", []))
        medium = len(by_severity.get("Medium", []))

        lines.append(
            f"Automated PHI scan identified **{len(self.violations)} violations** across "
            f"{len(self.scanned_files)} files: {critical} Critical, {high} High, {medium} Medium. "
            f"Immediate remediation required for Critical violations before next deployment. "
            f"All violations must be resolved to achieve HIPAA compliance."
        )
        lines += ["", "---", "", "## Violations by Severity", ""]

        for sev in ["Critical", "High", "Medium", "Low"]:
            items = by_severity.get(sev, [])
            if not items:
                continue
            lines.append(f"### {sev} ({len(items)})")
            lines.append("")
            for v in items:
                lines.append(f"- [ ] `{v.file_path}:{v.line_no}` — **{v.phi_name}** — {v.hipaa_rule}")
                lines.append(f"  - {v.context}")
                lines.append(f"  - Code: `{v.snippet[:100]}`")
                lines.append("")

        lines += [
            "---",
            "",
            "## PHI Flow Map",
            "",
            "| Service | PHI Types Accessed |",
            "|---------|-------------------|",
        ]
        for service, phi_types in self.phi_flow.items():
            lines.append(f"| `{service}` | {', '.join(sorted(phi_types))} |")

        lines += [
            "",
            "---",
            "",
            "## Compliance Checklist",
            "",
            "- [ ] All Critical violations resolved",
            "- [ ] All High violations resolved",
            "- [ ] Encryption at rest implemented (AES-256)",
            "- [ ] TLS 1.2+ enforced for all PHI transmission",
            "- [ ] Authentication on all PHI endpoints",
            "- [ ] PHI redacted in all log outputs",
            "- [ ] Audit trail implemented",
            "- [ ] All compliance tests passing",
            "",
            "---",
            "",
            "## Sign-off",
            "",
            "| Role | Name | Signature | Date |",
            "|------|------|-----------|------|",
            "| Compliance Officer | | | |",
            "| Engineering Lead | | | |",
            "| Security Architect | | | |",
            "",
            "---",
            "",
            "*Generated by IBM Bob PHI Compliance Scanner*",
        ]

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"[PHI Scanner] Markdown report saved: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="HIPAA PHI Compliance Scanner")
    parser.add_argument("--repo", required=True, help="Path to repository to scan")
    parser.add_argument("--output", default="../reports/audit-report.md",
                        help="Output path for Markdown report")
    parser.add_argument("--json", default=None, help="Output path for JSON report")
    args = parser.parse_args()

    scanner = PHIScanner(args.repo)
    scanner.scan()
    scanner.print_report()
    scanner.export_markdown(args.output)

    json_path = args.json or args.output.replace(".md", ".json")
    scanner.export_json(json_path)

    print(f"\n[PHI Scanner] Done. Reports saved to:")
    print(f"  Markdown : {args.output}")
    print(f"  JSON     : {json_path}")


if __name__ == "__main__":
    main()
