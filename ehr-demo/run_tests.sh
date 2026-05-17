#!/bin/bash
# Test runner script for EHR Demo
# Runs all tests and generates coverage report

set -e

echo "========================================="
echo "EHR Demo - Running All Tests"
echo "========================================="
echo ""

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "pytest not found. Installing..."
    pip install pytest pytest-cov
fi

# Run tests for each service
echo "Running patient-api tests..."
pytest patient-api/tests/ -v

echo ""
echo "Running billing-service tests..."
pytest billing-service/tests/ -v

echo ""
echo "Running audit-logger tests..."
pytest audit-logger/tests/ -v

echo ""
echo "========================================="
echo "Running all tests with coverage..."
echo "========================================="
pytest --cov=. --cov-report=term --cov-report=html

echo ""
echo "========================================="
echo "Test Summary"
echo "========================================="
echo "✓ All tests completed"
echo "✓ Coverage report generated in htmlcov/"
echo ""
echo "Note: Tests are designed to PASS, proving"
echo "that violations exist. This is intentional"
echo "for demo purposes."
echo "========================================="

# Made with Bob
