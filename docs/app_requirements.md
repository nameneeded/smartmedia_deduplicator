# ✅ Application Requirements (Starter Seed)

This document outlines the explicit, testable requirements for the Lean + LLM-Aware Project Starter Seed. Each requirement is designed to ensure that future projects using this seed follow consistent, modular, and token-aware practices.

---

## 📦 Core Structure

| ID   | Requirement                                                                 | Status     |
|------|------------------------------------------------------------------------------|------------|
| R1   | The project must contain a modular `src/` directory with clearly separated submodules | ✅ Done     |
| R2   | Logging must be configured using a `logging_config.yaml` file but disabled by default | ✅ Done     |
| R3   | A template Python file (`src/template_python_file.py`) must exist with logging setup | ✅ Done     |
| R4   | The `docs/` folder must contain structured documentation templates          | ✅ Done     |
| R5   | `scripts/generate_project_structure_tree.py` must output a timestamped `.md` file | ✅ Done     |
| R6   | Previous structure files must be backed up to `docs/previous/`              | ✅ Done     |
| R7   | A `philosophy.md` file must explain best practices and project values       | ✅ Done     |
| R8   | A script (`rename_project.py`) must allow renaming the project safely       | ⏳ Pending  |
| R9   | A `logs/README.md` must define the logging policy and rotation format       | ✅ Done     |
| R10  | Assistant stubs must exist for Logimus and Schematicus                      | ⏳ Pending  |
| R11  | A starter LLM seed file must exist to onboard a dev assistant (e.g., Bitwise) | ⏳ Pending |
| R12  | Git init and setup instructions must be clearly defined in a boot guide     | ⏳ Pending  |
| R13  | A `features/` folder inside `tests/` must provide BDD support using `behave` | ✅ Added    |
| R14  | A script (`rename_project.py`) must allow renaming the project safely via CLI | ✅ Done |

---

## 🧪 Testing Strategy

- `tests/test_smoke.py`: Confirms expected files and folders exist
- `tests/features/`: Contains Gherkin feature files and `behave` step definitions
- `behave` is used for interface-level behavior testing
- `pytest` is used for isolated unit tests

---

## 🔄 Versioning and Expansion

- This file will evolve as features and expectations grow
- Each requirement should be uniquely identifiable and auditable
- Future enhancements (e.g., CI hooks, assistant orchestration) will add new requirements