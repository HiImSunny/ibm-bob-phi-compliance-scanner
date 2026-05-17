@echo off
REM Quick-start demo script for IBM Bob Hackathon (Windows)
REM Runs PHI scanner and displays results

echo ==========================================
echo   PHI Compliance Scanner - Demo
echo   IBM Bob Hackathon 2026
echo ==========================================
echo.

REM Check if scanner exists
if not exist "scanner\phi_scanner.py" (
    echo Error: scanner\phi_scanner.py not found
    echo Please run this script from the project root directory
    exit /b 1
)

REM Run the scanner
echo Scanning ehr-demo for HIPAA PHI violations...
echo.
python scanner\phi_scanner.py --repo .\ehr-demo --output .\reports\demo-report.md

if errorlevel 1 (
    echo.
    echo Scanner failed. Please check the error above.
    exit /b 1
)

echo.
echo ==========================================
echo   Scan Complete!
echo ==========================================
echo.

REM Display summary
if exist "reports\demo-report.md" (
    echo Quick Summary:
    findstr "Violations found:" reports\demo-report.md
    echo.
    echo Reports generated:
    echo    - Markdown: reports\demo-report.md
    echo    - JSON:     reports\demo-report.json
    echo.
    echo Ready for demo!
    echo.
    echo Next steps:
    echo   1. Open reports\demo-report.md to review violations
    echo   2. Run: pytest scanner\generated_tests\ (if tests exist^)
    echo   3. Present findings to compliance team
) else (
    echo Warning: Report file not found
)

echo.
echo ==========================================

@REM Made with Bob
