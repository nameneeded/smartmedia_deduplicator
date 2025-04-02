# Project structure as of 2025-04-02 09:31:24

```text
.
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── README.md
├── config
│   └── settings.yaml
├── docs
│   ├── README.md
│   ├── app_requirements.md
│   ├── architecture.md
│   ├── gitflow.md
│   ├── llm_integration.md
│   ├── philosophy.md
│   ├── previous
│   │   ├── project_structure_20250329_123530.md
│   │   ├── project_structure_20250329_123632.md
│   │   ├── project_structure_20250329_180821.md
│   │   └── project_structure_20250402_093124.md
│   ├── project_structure.md
│   └── sequence.md
├── logs
│   ├── README.md
│   ├── api.log
│   └── app.log
├── requirements.txt
├── scripts
│   ├── README.md
│   ├── generate_project_structure_tree.py
│   ├── record_directory_listing.py
│   ├── rename_project.py
│   ├── rotate_logs.py
│   ├── seed_init.py
│   └── test_indexer.py
├── src
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── match.py
│   │   ├── models
│   │   │   └── file_record.py
│   │   └── routes
│   │       └── scan.py
│   ├── core
│   │   ├── indexer.py
│   │   ├── matcher.py
│   │   ├── scanner.py
│   │   └── utils.py
│   ├── logging
│   │   ├── logging_config.yaml
│   │   └── setup_logging.py
│   ├── template_python_file.py
│   └── utils
│       ├── config_loader.py
│       ├── file_scanner.py
│       └── load_test_env.py
├── tests
│   ├── .env.pictures
│   ├── .env.test_env
│   ├── .env.training_1-pics
│   ├── README.md
│   ├── __init__.py
│   ├── features
│   │   ├── environment.py
│   │   ├── sample.feature
│   │   ├── scan.feature
│   │   └── steps
│   │       └── test_scan.py
│   ├── resources
│   │   ├── Pictures_match_queues.json
│   │   ├── Pictures_match_sorted.json
│   │   ├── TRAINING_1-pics_match_queues.json
│   │   ├── TRAINING_1-pics_scan_baseline.json
│   │   └── pictures_scan_baseline.json
│   ├── test_curl_api.py
│   └── test_scan_api.py
└── update_logs
    ├── 20250329.md
    └── update_seeds
        ├── chat-neo-vs-chat-j.md
        ├── openai_memory_model.md
        ├── openai_memory_sequence.md
        ├── project_MultiLLMOrchestrationSystem-20250329.json
        ├── project_MultiLLMOrchestrationSystem-20250329.md
        ├── project_MultiLLMOrchestrationSystem-delta-MemoryUpdates.json
        ├── project_SmartMediaDeduplicator-20250329.json
        └── project_SmartMediaDeduplicator-20250329.md
```