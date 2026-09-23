# 🚀 Study CI/CD with Python 3.14 & GitHub Actions

A comprehensive, hands-on 4-week (20 working days) practical curriculum for learning **Continuous Integration and Continuous Delivery (CI/CD)** using **Python 3.14**, **`uv`**, and **GitHub Actions**.

---

## 📑 Table of Contents

- [Overview & Objectives](#-overview--objectives)
- [Repository Structure](#-repository-structure)
- [Quick Start: Local Environment with Python 3.14 & `uv`](#-quick-start-local-environment-with-python-314--uv)
- [4-Week Step-by-Step Study Plan (20 Working Days)](#-4-week-step-by-step-study-plan-20-working-days)
  - [Week 1: CI Foundations — Code Quality & Linting](#week-1-ci-foundations--code-quality--linting-days-15)
  - [Week 2: Automated Testing & Matrix Builds](#week-2-automated-testing--matrix-builds-days-610)
  - [Week 3: DevSecOps — SAST & Dependency Auditing](#week-3-devsecops--sast--dependency-auditing-days-1115)
  - [Week 4: Continuous Delivery (CD), Docker & Releases](#week-4-continuous-delivery-cd-docker--releases-days-1620)
- [GitHub Actions Workflows in this Repo](#-github-actions-workflows-in-this-repo)
- [Step-by-Step How-To Guides](#-step-by-step-how-to-guides)
  - [1. Testing CI with a Pull Request](#1-testing-ci-with-a-pull-request)
  - [2. Configuring GitHub Secrets & Environments](#2-configuring-github-secrets--environments)
  - [3. Triggering a Production Release with Git Tags](#3-triggering-a-production-release-with-git-tags)
- [Local Verification Commands](#-local-verification-commands)
- [CI/CD Best Practices & Key Takeaways](#-cicd-best-practices--key-takeaways)
- [Learning Milestones Checklist](#-learning-milestones-checklist)

---

## 🎯 Overview & Objectives

The goal of this repository is to take you from CI/CD basics to an automated, production-grade pipeline in **4 weeks** (excluding weekends and national holidays).

### What You Will Master:
1. **CI Foundations**: Automated code formatting (`black`), modern linting (`ruff`), and static typing (`mypy`) on Python 3.14.
2. **Automated Testing**: Unit & parameterized testing with `pytest`, coverage reports with `pytest-cov`, and GitHub Actions **Matrix Builds** across Python 3.12, 3.13, and 3.14.
3. **DevSecOps**: Static Application Security Testing (SAST) with `bandit`, dependency vulnerability scanning with `pip-audit`, and scheduled cron workflows.
4. **Continuous Delivery (CD)**: Python wheel packaging (`build`), Docker containerization with Python 3.14 (`Dockerfile`), deployment simulation across **Staging** and **Production**, environment secrets, and automated GitHub Releases on Git tags.

---

## 📂 Repository Structure

```text
study_ci_cd/
├── .github/
│   └── workflows/
│       ├── 01-lint-format.yml       # Week 1: Formatting, linting, type-checking (Python 3.14 + uv)
│       ├── 02-tests-matrix.yml      # Week 2: Matrix unit tests (3.12, 3.13, 3.14) & coverage artifacts
│       ├── 03-security-audit.yml    # Week 3: Bandit SAST & pip-audit dependency scans
│       └── 04-cd-release.yml        # Week 4: Packaging, Docker smoke test & release
├── src/
│   ├── __init__.py                  # Package marker
│   ├── calculator.py               # Math & logic functions with modern Python 3.14 type hints
│   ├── data_processor.py           # Data transformations & input sanitization
│   └── app.py                      # Main CLI application entrypoint
├── tests/
│   ├── __init__.py                  # Test package marker
│   ├── test_calculator.py          # Pytest unit & parameterized tests
│   ├── test_data_processor.py      # Data processing tests & edge cases
│   └── test_app.py                 # CLI integration tests
├── scripts/
│   ├── run_local_checks.sh         # Run all quality checks locally
│   └── mock_deploy.py              # Simulates staging/production deployment
├── Dockerfile                      # Application container definition (Python 3.14-slim)
├── pyproject.toml                  # Project metadata, pytest & tool configurations (Python 3.14)
├── requirements.txt                # Production runtime dependencies
├── requirements-dev.txt            # Development, linting & testing dependencies
├── .gitignore                      # Git ignore rules (includes .venv)
└── README.md                       # Study plan, documentation & guides
```

---

## ⚡ Quick Start: Local Environment with Python 3.14 & `uv`

This repository uses [`uv`](https://github.com/astral-sh/uv), an extremely fast Python package and virtual environment manager.

### 1. Create and Activate Python 3.14 Virtual Environment
Inside this repository:
```bash
# Install Python 3.14 using uv (if not already installed)
uv python install 3.14

# Create a virtual environment inside .venv targeting Python 3.14
uv venv --python 3.14 .venv

# Activate the virtual environment
# On macOS / Linux:
source .venv/bin/activate
# On Windows (PowerShell):
# .venv\Scripts\Activate.ps1
```

### 2. Install Dependencies
```bash
# Sync runtime and development dependencies into virtual environment
uv sync --extra dev
```

Alternatively, install in editable mode or from requirement files:
```bash
uv pip install -e ".[dev]"
# or
uv pip install -r requirements.txt -r requirements-dev.txt
```

### 3. Run the Application
```bash
# Run CLI summary calculation
python -m src.app --numbers 10 25 40 85

# Run CLI input sanitization
python -m src.app --sanitize "<script>alert('test')</script>"
```

### 4. Run Local CI Checks
```bash
# Run all formatters, linters, type checks, and tests in one command
chmod +x scripts/run_local_checks.sh
./scripts/run_local_checks.sh
```

---

## 📅 4-Week Step-by-Step Study Plan (20 Working Days)

> **Schedule Note**: This plan consists of 20 study days (5 days/week × 4 weeks). Weekends and national holidays are excluded so you can pace yourself sustainably.

```
       WEEK 1                 WEEK 2                 WEEK 3                 WEEK 4
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│  CI Foundations  │   │  Automated Tests │   │    DevSecOps     │   │   CD & Release   │
│  - Code Quality  │──>│  - Matrix Builds │──>│  - Bandit SAST   │──>│  - Docker Build  │
│  - Ruff & Black  │   │  - Pytest & Cov  │   │  - Pip Audit     │   │  - Environments  │
│  - Mypy Types    │   │  - Artifacts     │   │  - Cron Triggers │   │  - GitHub Tag Rel│
└──────────────────┘   └──────────────────┘   └──────────────────┘   └──────────────────┘
```

---

### Week 1: CI Foundations — Code Quality & Linting (Days 1–5)

#### 🎯 Weekly Objective
Understand CI principles, create your first GitHub Actions workflow, and enforce code quality and static typing automatically on Pull Requests.

| Day | Topic | Hands-on Tasks | Expected Output / Verification |
| :--- | :--- | :--- | :--- |
| **Day 1** | **CI/CD Core Concepts & Git Flow** | • Learn what CI/CD solves (integration hell, manual regressions).<br>• Understand Git branching models (`main`, `feature/*`).<br>• Initialize remote GitHub repo and push initial commit. | Repository initialized on GitHub with a clean commit history. |
| **Day 2** | **Fast Python Tooling with `uv`** | • Set up `.venv` using `uv venv`.<br>• Explore `pyproject.toml` configurations for `black` and `ruff`.<br>• Run `black --check src/` and `ruff check src/`. | `uv` virtual environment active; formatting and linting pass locally. |
| **Day 3** | **GitHub Actions Syntax & Architecture** | • Study workflow anatomy: `on:`, `jobs:`, `runs-on:`, `steps:`, `uses:`, `run:`.<br>• Learn about GitHub-hosted runners (`ubuntu-latest`).<br>• Inspect [.github/workflows/01-lint-format.yml](file:///.github/workflows/01-lint-format.yml). | Comprehend each line in the workflow YAML file. |
| **Day 4** | **First Automated Workflow & PR Triggers** | • Create a new git branch: `git checkout -b feature/test-ci`.<br>• Introduce a deliberate formatting issue in `src/calculator.py` (e.g., trailing whitespace or bad indentation).<br>• Push branch and open a Pull Request against `main`. | GitHub Actions detects format violation and marks PR with a ❌ red check. Fix the formatting, push, and see it turn ✅ green. |
| **Day 5** | **Static Type Checking & Branch Protection** | • Explore `mypy` configuration in `pyproject.toml`.<br>• Run `mypy src/` locally to check typing annotations.<br>• In GitHub Settings > Branches, enable **Branch Protection Rule** on `main` requiring the status check `Code Quality Checks` to pass before merging. | PRs cannot be merged into `main` unless all linting and type checks pass. |

---

### Week 2: Automated Testing & Matrix Builds (Days 6–10)

#### 🎯 Weekly Objective
Master automated test suites, test coverage thresholds, matrix execution across multiple Python versions, and workflow artifacts.

| Day | Topic | Hands-on Tasks | Expected Output / Verification |
| :--- | :--- | :--- | :--- |
| **Day 6** | **Unit Testing with Pytest** | • Study [tests/test_calculator.py](file:///tests/test_calculator.py) and [tests/test_data_processor.py](file:///tests/test_data_processor.py).<br>• Run `pytest -v` locally.<br>• Add a new math utility in [src/calculator.py](file:///src/calculator.py) and write a corresponding test. | All unit tests pass with detailed output. |
| **Day 7** | **Parameterized & Exception Testing** | • Use `@pytest.mark.parametrize` to test multiple inputs/outputs in a single test function.<br>• Write tests verifying exceptions using `pytest.raises(ValueError)`. | Clear, non-repetitive test code covering boundary cases. |
| **Day 8** | **Code Coverage Analysis** | • Run `pytest --cov=src --cov-report=term-missing`.<br>• Generate HTML coverage report using `--cov-report=html`.<br>• Inspect the generated `htmlcov/index.html` in your browser. | Achieve > 90% test coverage across all `src/` modules. |
| **Day 9** | **Matrix Builds in GitHub Actions** | • Inspect [.github/workflows/02-tests-matrix.yml](file:///.github/workflows/02-tests-matrix.yml).<br>• Learn `strategy.matrix` configuration across Python `3.12`, `3.13`, and `3.14`.<br>• Push a commit and observe 3 parallel jobs executing in GitHub Actions. | Simultaneous verification of Python version compatibility. |
| **Day 10** | **Workflow Artifacts & Summary Reports** | • Study `actions/upload-artifact@v4` in `02-tests-matrix.yml`.<br>• Download the `coverage-report-html` artifact zip file from the GitHub Actions run summary page.<br>• Extract and view the artifact. | Artifacts successfully uploaded from runner and accessible in GitHub UI. |

---

### Week 3: DevSecOps — SAST & Dependency Auditing (Days 11–15)

#### 🎯 Weekly Objective
Integrate security into CI (DevSecOps), conduct automated static application security scans, audit vulnerable packages, and set up cron schedules.

| Day | Topic | Hands-on Tasks | Expected Output / Verification |
| :--- | :--- | :--- | :--- |
| **Day 11** | **Introduction to DevSecOps & Shift-Left** | • Understand why security scanning belongs in the CI pipeline.<br>• Learn the difference between SAST (Static Analysis), DAST (Dynamic Analysis), and SCA (Software Composition Analysis). | Foundational knowledge of CI security practices. |
| **Day 12** | **Static Security Analysis with Bandit** | • Run `bandit -r src/ -ll` locally.<br>• Introduce a mock insecure pattern (e.g. `assert` in production logic or hardcoded secret) in a branch to see Bandit flag it.<br>• Understand how to configure Bandit skip rules. | Bandit SAST reports zero high/medium severity security issues. |
| **Day 13** | **Dependency Vulnerability Scanning (`pip-audit`)** | • Run `pip-audit -r requirements.txt` locally.<br>• Inspect how `pip-audit` queries the Python Packaging Advisory Database (PyPA). | Assurance that third-party packages have no known CVEs. |
| **Day 14** | **Scheduled CI Workflows (Cron)** | • Inspect the `schedule:` block in [.github/workflows/03-security-audit.yml](file:///.github/workflows/03-security-audit.yml).<br>• Learn POSIX cron syntax (`0 6 * * 1` = every Monday at 06:00 UTC).<br>• Trigger the security workflow manually via `workflow_dispatch`. | Security scan runs automatically on schedule without requiring a git push. |
| **Day 15** | **CI Caching & Performance Optimization** | • Learn how `astral-sh/setup-uv` caches uv dependencies.<br>• Compare workflow execution time with cache hit vs cache miss.<br>• Optimize workflow runtime. | Fast, cached CI job execution (typically < 30 seconds). |

---

### Week 4: Continuous Delivery (CD), Docker & Releases (Days 16–20)

#### 🎯 Weekly Objective
Build distributable Python packages, containerize with Docker, manage GitHub Environments and Secrets, and automate releases.

| Day | Topic | Hands-on Tasks | Expected Output / Verification |
| :--- | :--- | :--- | :--- |
| **Day 16** | **Python Packaging (Wheel & sdist)** | • Run `python -m build` locally to generate `dist/*.whl` and `dist/*.tar.gz`.<br>• Inspect metadata and wheel archive contents.<br>• Understand how wheels are published to PyPI or private artifact registries. | Clean build artifacts produced in `dist/`. |
| **Day 17** | **Containerization with Docker** | • Review [Dockerfile](file:///Dockerfile).<br>• Build image locally: `docker build -t study-ci-cd:latest .`<br>• Run container: `docker run --rm study-ci-cd:latest`. | Docker container builds and executes CLI successfully. |
| **Day 18** | **GitHub Environments & Secrets** | • Navigate to GitHub Repo > **Settings** > **Environments**.<br>• Create two environments: `staging` and `production`.<br>• Configure required reviewers (manual approval gate) for `production`.<br>• Add a repository secret `DEPLOY_API_TOKEN`. | Safe deployment gate configured with access control and secret protection. |
| **Day 19** | **Continuous Delivery Pipeline** | • Study [.github/workflows/04-cd-release.yml](file:///.github/workflows/04-cd-release.yml) and [scripts/mock_deploy.py](file:///scripts/mock_deploy.py).<br>• Trigger the workflow manually with `workflow_dispatch` selecting `staging`.<br>• Observe multi-stage pipeline: Build -> Staging Deploy -> Production Deploy. | Multi-stage CD pipeline executed with staged progression. |
| **Day 20** | **Automated GitHub Releases with Git Tags & Capstone** | • Create a semver git tag: `git tag -a v1.0.0 -m "Release version 1.0.0"`.<br>• Push tag: `git push origin v1.0.0`.<br>• Watch `04-cd-release.yml` automatically build artifacts, deploy, and publish a GitHub Release with auto-generated changelog.<br>• **Capstone Review**: Review all 4 workflows! | Official GitHub Release published with attached wheel and release notes. 🎓 |

---

## 🛠 GitHub Actions Workflows in this Repo

| Workflow File | Trigger Events | Purpose / Actions |
| :--- | :--- | :--- |
| [`01-lint-format.yml`](file:///.github/workflows/01-lint-format.yml) | `push`, `pull_request` on `main`, `develop` | Runs `black --check`, `ruff check`, and `mypy` static type analysis. |
| [`02-tests-matrix.yml`](file:///.github/workflows/02-tests-matrix.yml) | `push`, `pull_request` on `main`, `develop` | Runs `pytest` with coverage across Python 3.12, 3.13, 3.14 matrix and uploads HTML coverage artifact. |
| [`03-security-audit.yml`](file:///.github/workflows/03-security-audit.yml) | `push` on `main`, Weekly Cron, Manual Dispatch | Runs `bandit` SAST security scans and `pip-audit` dependency vulnerability checks. |
| [`04-cd-release.yml`](file:///.github/workflows/04-cd-release.yml) | Git tag `v*.*.*`, Manual Dispatch | Builds wheel distribution, tests Docker build, deploys to Staging/Production, and publishes GitHub Release. |

---

## 📖 Step-by-Step How-To Guides

### 1. Testing CI with a Pull Request
1. Create a feature branch:
   ```bash
   git checkout -b feature/add-new-metric
   ```
2. Add a new method in [src/calculator.py](file:///src/calculator.py):
   ```python
   @staticmethod
   def percentage(part: float, whole: float) -> float:
       """Calculate percentage."""
       if whole == 0:
           raise ValueError("Whole cannot be zero.")
       return (part / whole) * 100
   ```
3. Add a unit test in [tests/test_calculator.py](file:///tests/test_calculator.py):
   ```python
   def test_percentage(self) -> None:
       assert Calculator.percentage(25, 100) == 25.0
   ```
4. Verify locally:
   ```bash
   ./scripts/run_local_checks.sh
   ```
5. Commit, push, and create a PR on GitHub:
   ```bash
   git add src/calculator.py tests/test_calculator.py
   git commit -m "feat: add percentage method with unit tests"
   git push origin feature/add-new-metric
   ```
6. Open your browser to the GitHub repository and click **Create Pull Request**. Watch the checks run!

---

### 2. Configuring GitHub Secrets & Environments
1. Go to your GitHub repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2. Click **New repository secret**.
   - Name: `DEPLOY_API_TOKEN`
   - Value: `my-super-secret-token-12345`
3. Go to **Settings** -> **Environments**:
   - Create environment `staging`.
   - Create environment `production` (optionally enable *Required reviewers*).

---

### 3. Triggering a Production Release with Git Tags
1. Ensure your `main` branch is clean and all tests pass.
2. Create an annotated semantic version tag:
   ```bash
   git tag -a v1.0.0 -m "Release v1.0.0: Initial stable release"
   ```
3. Push the tag to GitHub:
   ```bash
   git push origin v1.0.0
   ```
4. GitHub Actions will trigger `04-cd-release.yml`, package your application, execute staging and production deployment steps, and automatically publish a GitHub Release with downloadable `.whl` and `.tar.gz` distribution files.

---

## 🔍 Local Verification Commands

| Command | Description |
| :--- | :--- |
| `uv run pytest` | Run all unit tests |
| `uv run pytest --cov=src --cov-report=term-missing` | Run tests with terminal coverage summary |
| `uv run black --check src tests` | Check code formatting without modifying files |
| `uv run black src tests` | Auto-format Python code |
| `uv run ruff check src tests` | Lint Python source code |
| `uv run mypy src` | Check static types |
| `uv run bandit -r src -ll` | Run SAST security check |
| `uv run python -m build` | Build wheel and source distributions |
| `./scripts/run_local_checks.sh` | Run all quality and test checks sequentially |

---

## 💡 CI/CD Best Practices & Key Takeaways

1. **Virtual Environment Isolation & PEP 668**:
   - Modern Linux runners (Ubuntu 24.04+) enforce PEP 668 (`EXTERNALLY-MANAGED`) to protect system Python packages.
   - Always use `astral-sh/setup-uv` with `python-version: ...` and `uv sync` to isolate dependencies within `.venv` rather than installing into global system directories.

2. **Tool Execution with `uv run`**:
   - Prefix commands with `uv run` (e.g., `uv run pytest`, `uv run black`) or export `$GITHUB_WORKSPACE/.venv/bin` into `$GITHUB_PATH` so that all installed tools are immediately found in CI.

3. **Multi-Version Syntax Compatibility (Python 3.12 - 3.14)**:
   - When handling multiple exception types, always enclose them in parentheses: `except (json.JSONDecodeError, TypeError):`.
   - Keep tool target versions (e.g., `[tool.black]` and `[tool.ruff]`) aligned with the minimum supported matrix version (`py312`).

4. **Deterministic Builds with `uv.lock`**:
   - Keep `uv.lock` checked into Git for reproducible CI runs and fast cached installations.

---

## 🏆 Learning Milestones Checklist

- [ ] **Week 1**: All PRs automatically linted and type-checked before merge.
- [ ] **Week 2**: Unit tests running across Python 3.12, 3.13, 3.14 with > 80% coverage.
- [ ] **Week 3**: Security scanning running on commit and scheduled weekly cron.
- [ ] **Week 4**: Automated Docker build, environment deployment, and GitHub Releases on tag.
