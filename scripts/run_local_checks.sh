#!/usr/bin/env bash
set -e

RUNNER=""
if command -v uv >/dev/null 2>&1; then
    RUNNER="uv run"
fi

echo "=== 1. Checking Code Formatting with Black ==="
${RUNNER} black --check src tests || { echo "Run 'uv run black src tests' to format code."; exit 1; }

echo "=== 2. Running Lint Checks with Ruff ==="
${RUNNER} ruff check src tests

echo "=== 3. Running Static Type Checker (mypy) ==="
${RUNNER} mypy src

echo "=== 4. Running Security Checks (bandit) ==="
${RUNNER} bandit -r src -ll

echo "=== 5. Running Pytest Suite with Coverage ==="
${RUNNER} pytest --cov=src --cov-report=term-missing --cov-fail-under=80

echo "🎉 All local CI checks passed successfully!"
