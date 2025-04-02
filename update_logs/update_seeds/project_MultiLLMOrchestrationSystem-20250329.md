**Project Name**: Multi-LLM Orchestration System

**Status**: ✅ Active
**Last Updated**: 2025-03-29

---

### 🧠 Purpose
To build a **modular, scalable system** that allows a central LLM to coordinate with multiple domain-specialized LLM instances, while managing token context, memory, and user workflow intelligently.

---

### 🧰 Key Components & Architecture

#### 🧭 Coordinator LLM: **Charlar**
- Central conversational brain
- Retains high-level personal memory and manages topic switching
- Responsible for memory-aware context delegation and orchestration

#### 🧠 Developer LLM: **Bitwise**
- Role: Code development partner
- Model: `gpt-3.5-turbo-0125`
- Functions: Writes, refactors, and understands modular Python architecture

#### 📓 System Documentation LLM: **Schematicus**
- Role: Architecture and documentation partner
- Handles Mermaid diagrams, system specs, and project structure rendering

#### 📜 Logging Assistant: **Logimus**
- Tracks all code actions, architectural changes, and assistant usage
- Maintains metadata for traceability and auditing

#### 📡 Backend Interface: **TalkyToaster**
- Acts as a non-LLM coordination layer
- Manages LLM-to-LLM handshakes, passes structured data packets
- Will evolve from rule-based to adaptive coordination

---

### 🏗️ Project Structure & Tools
- **Folder layout** includes: `src/core/`, `src/orchestration/`, `seeds/`, `docs/`, `scripts/`, `tests/`
- Tools include:
  - 🧪 Pytest + Behave (BDD)
  - 📦 OpenAI Python SDK
  - ⚙️ GitHub Actions (CI)
  - 📂 JSON seeds for LLM initialization
  - 📋 `project_structure.txt` for auto-updating file tree

---

### 🧮 Core Concepts

#### 🔀 `context_bundles`
- Contain transferable context across LLMs
- Includes domain-tagged tokens, heuristics, and memory anchors

#### 🔗 `token_streams`
- Sequential logical units (e.g., code block, conversation segment)
- Tagged and weighted for compression/retention

#### 🧩 `abridged_tokens`
- Summarized forms of older content
- Helps reduce token weight while maintaining core meaning

#### 🔁 `delta_seed`
- Encodes changes since last context sync
- Used to update LLM memory incrementally without full reseed

---

### 🔄 Current Workflow Summary
1. Charlar coordinates the project direction and creates seed context
2. Bitwise handles code creation and modular development
3. Schematicus documents the project in Markdown and Mermaid.js
4. Logimus logs system events with assistant IDs and thread references
5. TalkyToaster handles coordination between agents and context passes

---

### 📌 Current Objectives
- Finalize clean architecture with full assistant division
- Implement `delta_seed` support for incremental updates
- Formalize `talkytoaster_protocol.json` for handshake structure
- Automate memory offloading with pointer caching

---

### ✅ Next Steps
- Seed Schematicus and Logimus with updated `project_structure.md`
- Implement `token_stream` compression model
- Add config-driven assistant initializer in `scripts/seed_init.py`
- Sync Bitwise and TalkyToaster roles in orchestration layer

---
