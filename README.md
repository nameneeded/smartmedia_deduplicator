# 🧱 Lean + LLM-Aware Project Starter Seed

This is a minimal, modular, and thoughtfully structured starter project for Python-based applications. It’s designed to promote clean architecture, reliable tooling, and optional integration with LLM-based development and documentation assistants.

---

## 🚀 Quickstart

### 1. Clone the Repository
```bash
git clone <your-project-url> my-project
cd my-project
```

### 2. Install Dependencies
> This project uses standard Python tools and optional testing/dev libraries.
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Initialize Logging (optional)
Logging is configured but disabled by default. You can enable it by calling:
```python
from logging.setup_logging import setup_logging
setup_logging()
```

---

## 📁 Project Layout

| Path | Purpose |
|------|---------|
| `src/` | Main application code (organized by concern) |
| `scripts/` | CLI tools and setup scripts |
| `docs/` | Architecture, requirements, and philosophy documentation |
| `logs/` | Runtime logs (rotated automatically when active) |
| `seeds/` | Optional LLM seed files for development/documentation agents |
| `tests/` | Pytest unit tests and Behave BDD feature tests |

---

## 🧪 Testing

### ✅ Pytest (unit tests)
```bash
pytest
```

### ✅ Behave (BDD / Gherkin-style features)
```bash
behave tests/features/
```

---

## 🤖 LLM Integration (Optional)

If working with AI assistants like Bitwise, Schematicus, or Logimus:
- See [`docs/llm_integration.md`](docs/llm_integration.md) for setup and purpose
- Seed files for assistants are stored in `seeds/`
- These tools assist with refactoring, logging review, and documentation—not application logic

---

## 🛠 First Customization Step

If you’re starting a new project based on this template:
1. Unzip the seed archive or clone the repo
2. Run the project rename script:
```bash
python scripts/rename_project.py -n my_actual_project_name
```
3. Initialize a new Git repository:
```bash
rm -rf .git
git init
git add .
git commit -m "Initial commit from starter seed"
```

---

## 📜 Philosophy

This project favors:
- Modular, testable design
- LLM-aware but not LLM-dependent workflows
- Logging, documentation, and version control from day one

See [`docs/philosophy.md`](docs/philosophy.md) for more.

---

## 📬 Questions or Suggestions?

This seed is designed to evolve. If you're improving it, building on it, or running into issues—document it! This is a gift to future-you.