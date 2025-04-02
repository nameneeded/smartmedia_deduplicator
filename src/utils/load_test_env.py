# src/utils/load_test_env.py

from dotenv import dotenv_values
from pathlib import Path
import random

def load_test_env(env_path: Path = Path("tests/.env.training_1-pics")) -> dict:
    print("🔧 Loading test environment config...")
    raw = dotenv_values(env_path)
    base = raw.get("BASE", "").strip()

    scan_template = raw.get("TEST_SCAN_PATH", "").strip()
    baseline_template = raw.get("TEST_BASELINE_FILE", "").strip()

    print(f"🧪 Templates → Scan: {scan_template}, Baseline: {baseline_template}")

    if not scan_template or not baseline_template:
        raise ValueError("Missing TEST_SCAN_PATH or TEST_BASELINE_FILE in env config")

    # Replace placeholders
    scan_path = Path(scan_template.replace("{BASE}", base)).expanduser().resolve()
    baseline_file = baseline_template.replace("{BASE}", base)
    match_file = f"tests/resources/{base}_match_queues.json"

    # Grab a random file from the target directory
    random_file = ""
    if scan_path.exists():
        print(f"📂 Resolved scan path: {scan_path}")
        all_files = [f for f in scan_path.rglob("*") if f.is_file()]
        if all_files:
            random_file = str(random.choice(all_files).resolve())

    resolved = {
        "TEST_SCAN_PATH": str(scan_path),
        "TEST_BASELINE_FILE": baseline_file,
        "TEST_MATCH_FILE": match_file,
        "TEST_RANDOM_FILE": random_file
    }

    # Write resolved output to unified env file
    env_dump_path = Path("tests/.env.test_env")
    with open(env_dump_path, "w") as f:
        for key, val in resolved.items():
            f.write(f"{key}={val}\n")

    print(f"✅ Environment written to: {env_dump_path}")
    return resolved

if __name__ == "__main__":
    env = load_test_env()
    print("✅ Loaded Environment:")
    for k, v in env.items():
        print(f"  {k}: {v}")