# tests/test_curl_api.py
import subprocess
import json
from src.utils.load_test_env import load_test_env

def test_curl_directory_scan():
    env = load_test_env()
    url = f"http://127.0.0.1:8000/scan?path={env['TEST_SCAN_PATH']}"
    result = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
    assert result.returncode == 0, "Curl command failed"
    data = json.loads(result.stdout)
    assert isinstance(data, list)
    assert len(data) > 0

def test_curl_single_file():
    env = load_test_env()
    url = f"http://127.0.0.1:8000/scan/item?path={env['TEST_SCAN_PATH']}&target={env['TEST_RANDOM_FILE']}"
    result = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
    assert result.returncode == 0, "Curl command failed"
    data = json.loads(result.stdout)
    assert "path" in data
    assert "size_bytes" in data