#!/usr/bin/env bash
set -e

echo "=== 1. Checking Code Formatting with Black ==="
black --check src tests || { echo "Run 'black src tests' to format code."; exit 1; }

echo "=== 2. Running Lint Checks with Ruff / Flake8 ==="
ruff check src tests

echo "=== 3. Running Static Type Checker (mypy) ==="
mypy src

echo "=== 4. Running Security Checks (bandit) ==="
bandit -r src -ll

echo "=== 5. Running Pytest Suite with Coverage ==="
pytest --cov=src --cov-report=term-missing --cov-fail-under=80

echo "🎉 All local CI checks passed successfully!"
