# 🛠️ Project Scripts

This folder contains CLI tools and developer utilities used to maintain or customize the project. These scripts support automation, standardization, and assistant interaction workflows.

---

## 📋 Available Scripts

### 🔄 `generate_project_structure_tree.py`
Generates a Markdown-based tree of the current project structure.

- Outputs: `docs/project_structure.md`
- Backs up previous structure files to `docs/previous/`
- Ignores virtualenv, build, and cache folders by default

#### Usage:
```bash
python scripts/generate_project_structure_tree.py
```

---

### 🧼 `rename_project.py` *(in development)*
Will safely rename all references to the template project (`smartmedia_deduplicator`) across source files, docs, and config stubs.

- Intended to be run immediately after unzipping the seed for a new project
- Will support a `-n` or `--name` argument for project renaming

#### Example (planned usage):
```bash
python scripts/rename_project.py -n my_actual_project_name
```

---

### 🧪 `pre-commit` Integration

If you're using Git, install and enable the pre-commit hooks defined in `.pre-commit-config.yaml`.

These will help ensure:
- Clean formatting (`black`, `isort`)
- Markdown is valid and readable (`markdownlint`)
- No stray whitespace or debug statements

#### Setup:
```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files  # optional: run on existing code
```

---

### 🧠 LLM Integration Scripts (Optional / Advanced)

The following scripts support interaction with LLMs like Bitwise, Logimus, and Schematicus if you are using the Multi-LLM Orchestration system:

- `ingest_file_to_assistant.py`
- `request_assistant_update.py`
- `create_llm_instance.py`
- `run_assistant_thread.py`

See `docs/llm_integration.md` for more details.

---

## 📌 Notes

- All scripts should be **non-destructive** and safely testable
- Logging behavior is optional and controlled via `src/logging/setup_logging.py`
- Scripts can assume a standard project structure rooted at the same level as `src/`, `docs/`, and `tests/`

---

## 📝 Tips

- While not required, this folder includes an `__init__.py` file to allow future imports (e.g., if any CLI tools need to be reused as modules).
- This has no effect on running the scripts directly, but enables flexibility and better IDE/linter support down the line.

---

## 🔁 `rotate_logs.py`
Manually forces rotation of the active log file defined in `logs/app.log`.

Useful for CI pipelines, clean resets, or testing rotation behavior.

```bash
python scripts/rotate_logs.py