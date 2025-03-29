import logging.config
import yaml
import os

def setup_logging(config_path="src/logging/logging_config.yaml"):
    if not os.path.exists(config_path):
        print(f"⚠️  Logging config not found at {config_path}")
        return

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)