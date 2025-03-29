from dotenv import dotenv_values
from pathlib import Path
import random

def load_test_env(env_path: Path = Path("tests/.env.training_1-pics")) -> dict:
    print("hi")
    raw = dotenv_values(env_path)
    base = raw.get("BASE", "")

    scan_template = raw.get("TEST_SCAN_PATH", "")
    baseline_template = raw.get("TEST_BASELINE_FILE", "")
    print(f"{scan_template} and {baseline_template}")

    if not scan_template or not baseline_template:
        raise ValueError("Missing TEST_SCAN_PATH or TEST_BASELINE_FILE in env config")

    scan_path = Path(scan_template.replace("{BASE}", base)).expanduser()
    baseline_file = baseline_template.replace("{BASE}", base)

    # Pick a random file inside the scan dir
    random_file = None
    if scan_path.exists():
        print(f"Resolved path: {scan_path}")
        all_files = [f for f in scan_path.rglob("*") if f.is_file()]
        if all_files:
            random_file = str(random.choice(all_files).resolve())

    # ✅ Build resolved dictionary first
    resolved = {
        "TEST_SCAN_PATH": str(scan_path),
        "TEST_BASELINE_FILE": baseline_file,
        "TEST_RANDOM_FILE": random_file or ""
    }

    # ✅ Now write to .env.test_env
    env_dump_path = Path("tests/.env.test_env")
    with open(env_dump_path, "w") as f:
        for key, val in resolved.items():
            f.write(f"{key}={val}\n")

    print(f"[Env Sync] Wrote resolved test env to: {env_dump_path}")
    return resolved

if __name__ == "__main__":
    env = load_test_env()
    print("✅ Loaded Environment:")
    for k, v in env.items():
        print(f"  {k}: {v}")