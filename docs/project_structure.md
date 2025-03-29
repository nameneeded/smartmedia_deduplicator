# Project structure as of 2025-03-28 17:47:32

```text
.
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── README.md
├── docs
│   ├── README.md
│   ├── app_requirements.md
│   ├── architecture.md
│   ├── bitwise_seed_yyyymmdd.json
│   ├── gitflow.md
│   ├── llm_integration.md
│   ├── philosophy.md
│   ├── previous
│   ├── project_structure.md
│   └── sequence.md
├── logs
│   └── README.md
├── requirements.txt
├── scripts
│   ├── README.md
│   ├── generate_project_structure_tree.py
│   ├── rename_project.py
│   ├── rotate_logs.py
│   └── seed_init.py
├── seeds
│   ├── logimus_seed.json
│   ├── schematicus_seed.json
│   └── starter_assistant_seed.json
├── src
│   ├── __init__.py
│   ├── cli
│   ├── core
│   ├── logging
│   │   ├── logging_config.yaml
│   │   └── setup_logging.py
│   ├── orchestration
│   │   ├── logimus_agent.py
│   │   └── schematicus_agent.py
│   ├── template_python_file.py
│   ├── ui
│   └── utils
└── tests
    ├── README.md
    ├── __init__.py
    ├── features
    │   ├── environment.py
    │   ├── sample.feature
    │   └── steps
    │       └── sample_steps.py
    └── test_smoke.py
```