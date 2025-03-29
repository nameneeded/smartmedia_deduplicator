import yaml
from pathlib import Path

def load_settings(path: Path = Path("config/settings.yaml")) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)