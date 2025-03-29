# 🧪 Project Testing Overview

This folder contains all automated tests for the project, including both unit tests and behavior-driven development (BDD) tests.

---

## ✅ Test Frameworks

### 1. Pytest (Unit + Functional Testing)

- Located in the root of `tests/` (e.g., `test_smoke.py`)
- Used for:
  - Verifying core logic and reusable components
  - Fast, isolated, logic-driven tests
  - Test coverage measurement (via `pytest-cov` if added)

#### 🔧 Run All Pytest Tests:
```bash
pytest
```

---

### 2. Behave (Gherkin / BDD)

- Located in `tests/features/`
- Used for:
  - Describing behavior using Given/When/Then syntax
  - Expanding user stories into testable feature specs
  - Testing system-level workflows or interface behavior

#### 🔧 Run All Behave Tests:
```bash
behave tests/features/
```

#### 📁 Folder Layout:
```bash
tests/features/
├── sample.feature           # Gherkin-based feature description
├── steps/
│   └── sample_steps.py      # Step definitions (Python bindings)
├── environment.py           # Optional hooks (before_scenario, etc.)
```

---

## 📌 Best Practices

| Topic | Practice |
|-------|----------|
| 🧱 Structure | Keep unit and BDD tests organized and separate |
| 🔍 Naming | Use descriptive names for features and test files |
| 🧪 Coverage | Favor pytest for logic-heavy components |
| 🤝 Clarity | Favor behave for narrative-style interface scenarios |
| 💡 Incrementality | Tie new requirements (`app_requirements.md`) to Gherkin features when possible |

---

## 🚧 Future Enhancements

- `conftest.py` for shared fixtures
- `tox` or `nox` setup for matrix testing (optional)
- Test result summary integration into CI