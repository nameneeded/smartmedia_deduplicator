# 🧠 Philosophy & Best Practices

This document captures the design values, conventions, and evolving best practices behind this project starter seed. It serves as a reference for why the system is structured the way it is, and how new contributors (human or AI) should approach development.

---

## 🔹 Core Principles

### 1. **Structure Before Automation**
We prioritize clean, modular structure before introducing tooling or automation. The foundation should be clear even without advanced agents or CI/CD support.

### 2. **LLM-Aware, Not LLM-Dependent**
While the starter seed is designed to work with AI assistants, it does not require them. LLMs are invited to participate—but not assumed to be present.

### 3. **Separation of Concerns**
Code is divided by purpose:
- `src/core/`: Reusable logic and low-level abstractions
- `src/cli/`: User-facing scripts or entry points
- `src/logging/`: Logging infrastructure
- `src/orchestration/`: Agent and seed integration points

### 4. **Token-Aware Offloading**
LLMs like Bitwise do not retain long memory. They work from context provided via seeds and shared documents (see: `docs/`). This pattern minimizes token usage while maximizing recall and modularity.

---

## 🛠 Technical Commitments

- ✅ Logging is configured but not enabled by default
- ✅ File tree generation is automated and versioned
- ✅ Project renaming will be script-driven (`rename_project.py`)
- ✅ Seeds provide structured, reproducible assistant onboarding
- ✅ Logs are rotated and not bloated by default verbosity

---

## 📚 Documentation Strategy

- Markdown-first
- Git-friendly (versionable and readable)
- References to assistants, when present, are clear and scoped

---

## 🧩 Evolving Practices (To Be Tracked)

- CLI invocation patterns
- Assistant delta/handback format
- Git workflow and CI pipeline standards
- Test coverage thresholds (TBD in `app_requirements.md`)
- Naming conventions for agents, seeds, and docs

---

This philosophy grows with each iteration. If something feels right, document it here before it becomes a habit.