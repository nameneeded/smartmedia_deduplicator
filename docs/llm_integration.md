# 🤖 LLM Integration Strategy (Early Model)

This document outlines the current roles, integration points, and interaction strategy for Large Language Models (LLMs) used alongside this project. These assistants are not part of the application itself, but may support its development, testing, or monitoring as part of the **DevOps** or **Orchestration** layer.

⚠️ This model is in early exploration and may evolve significantly over time.

---

## 🧠 Assistant Roles

| Assistant | Domain | DevOps or Application | Notes |
|----------|--------|------------------------|-------|
| **Bitwise** | Software development logic, refactoring, coding best practices | DevOps | Instantiated via UI; specialized for Python & architecture-aware coding support |
| **Schematicus** | Documentation generation & architectural alignment | DevOps | Generates `*.md`, `*.mmd`, and project structure diagrams; supports seed summary/translation |
| **Logimus** | Logging insights, monitoring, trace summaries | Application | Tracks real-time run activity if integrated; part of in-system telemetry |

---

## 🛠️ Assistant: Bitwise (Development Assistant)

**Bitwise** is an LLM development partner instantiated by the user (via UI or API) with a seed to onboard context.

### 🎯 Purpose
- Writing, debugging, and refactoring Python code
- Supporting modular architecture and best practices (e.g., SOLID, clean CLI tools)
- Helping structure seed-based orchestration logic
- Maintaining consistency across modules and assisting in code reviews

### 🧰 Instantiation Strategy

Bitwise is initialized using:
- A structured seed file (e.g., `bitwise_seed_YYYY-MM-DD.json`)
- A copy of the current `project_structure.md`
- Optional references to architecture, philosophy, or requirements docs

> Seed is used to **set initial identity, tone, scope, and responsibilities**.

### 🧭 Model Selection

Bitwise should be run using the **latest stable OpenAI model available through the UI** unless:
- A specialized dev-tuned model (e.g., `gpt-4-code`) is available and supported
- The user overrides it for performance, capability, or cost reasons

**Default Recommendation (as of seed creation):**
```json
"model": "gpt-4-turbo"  // or "gpt-3.5-turbo-0125" for fast refactor-only work
```

---

## 📋 Bitwise Communication Pattern

Bitwise is tuned to:
- ✅ Acknowledge all requests and seek clarifications when unclear
- ✅ Provide structured, tested, annotated code
- ✅ Suggest but not impose architectural decisions (defers to Schematicus or user)
- ✅ Stay quiet on documentation unless specifically asked

---

## 🔁 Interaction Cycle

1. Seed is created and used to instantiate Bitwise
2. File context (e.g., `project_structure.md`) is uploaded or passed
3. User iterates with Bitwise to complete tasks (e.g., `rename_project.py`)
4. Bitwise may produce delta summaries for Charlar to ingest
5. Charlar performs offload/purge cycles to retain memory efficiency

---

## 🧩 Next Assistants to Define

- `Schematicus` (seed-based doc/diagram generation)
- `Logimus` (in-app or pseudo-agent logging + analysis)