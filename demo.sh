#!/bin/bash
# Quick-start demo script for IBM Bob Hackathon
# Runs PHI scanner and displays results

echo "=========================================="
echo "  PHI Compliance Scanner - Demo"
echo "  IBM Bob Hackathon 2026"
echo "=========================================="
echo ""

# Check if scanner exists
if [ ! -f "scanner/phi_scanner.py" ]; then
    echo "❌ Error: scanner/phi_scanner.py not found"
    echo "   Please run this script from the project root directory"
    exit 1
fi

# Run the scanner
echo "🔍 Scanning ehr-demo for HIPAA PHI violations..."
echo ""
python scanner/phi_scanner.py --repo ./ehr-demo --output ./reports/demo-report.md

# Check if scan succeeded
if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Scanner failed. Please check the error above."
    exit 1
fi

echo ""
echo "=========================================="
echo "  Scan Complete!"
echo "=========================================="
echo ""

# Display summary
if [ -f "reports/demo-report.md" ]; then
    echo "📊 Quick Summary:"
    grep "Violations found:" reports/demo-report.md | head -1
    echo ""
    echo "📄 Reports generated:"
    echo "   - Markdown: reports/demo-report.md"
    echo "   - JSON:     reports/demo-report.json"
    echo ""
    echo "✅ Ready for demo!"
    echo ""
    echo "Next steps:"
    echo "  1. Open reports/demo-report.md to review violations"
    echo "  2. Run: pytest scanner/generated_tests/ (if tests exist)"
    echo "  3. Present findings to compliance team"
else
    echo "⚠️  Warning: Report file not found"
fi

echo ""
echo "=========================================="

# Made with Bob
