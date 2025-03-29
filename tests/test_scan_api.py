import json
import pytest
from pathlib import Path
from fastapi.testclient import TestClient
from src.api.main import app
from src.utils.load_test_env import load_test_env

client = TestClient(app)

env = load_test_env()
BASELINE_PATH = env["TEST_SCAN_PATH"]
TEST_BASELINE_FILE = env["TEST_BASELINE_FILE"]

#BASELINE_PATH = Path("tests/resources/TRAINING_1-pics_scan_baseline.json")

@pytest.fixture(scope="module")
def baseline_data():
    with open(TEST_BASELINE_FILE, "r") as f:
        return json.load(f)

def test_scan_full_list_matches_baseline(baseline_data):
    response = client.get("/scan", params={"path": f"{BASELINE_PATH}"})
    assert response.status_code == 200
    api_data = response.json()
    assert len(api_data) == len(baseline_data)

def test_scan_single_file_match(baseline_data):
    sample = baseline_data[0]
    params = {
        "path": f"{BASELINE_PATH}",
        "target": sample["path"]
    }
    response = client.get("/scan/item", params=params)
    assert response.status_code == 200
    result = response.json()
    for key in ("path", "size_bytes", "type"):
        assert result[key] == sample[key]
    # Allow fuzzy match on timestamp (minor formatting differences)
    assert sample["modified"][:19] in result["modified"]
