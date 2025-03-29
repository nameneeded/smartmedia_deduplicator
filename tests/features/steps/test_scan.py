# tests/features/steps/sample_steps.py

import requests
import json
import subprocess
from behave import given, when, then

@given("the API is running")
def step_impl(context):
    # Could be extended later to poll the server
    context.base_url = "http://127.0.0.1:8000"
    print(f"[Behave] Using API at {context.base_url}")

@when("I request a scan of the directory")
def step_impl(context):
    path = context.env["TEST_SCAN_PATH"]
    response = requests.get(f"{context.base_url}/scan", params={"path": path})
    context.response = response
    context.data = response.json()

@then("I should receive a list of files")
def step_impl(context):
    assert context.response.status_code == 200
    assert isinstance(context.data, list)
    assert len(context.data) > 0

@then("the number of files should match the expected baseline")
def step_impl(context):
    baseline_path = context.env["TEST_BASELINE_FILE"]
    with open(baseline_path, "r") as f:
        baseline = json.load(f)
    assert len(context.data) == len(baseline)

@then("each file in the response should include path, size, modified, and type")
def step_impl(context):
    for item in context.data:
        assert "path" in item
        assert "size_bytes" in item
        assert "modified" in item
        assert "type" in item

@when("I request scan metadata for a random file")
def step_impl(context):
    path = context.env["TEST_SCAN_PATH"]
    target = context.env["TEST_RANDOM_FILE"]
    response = requests.get(f"{context.base_url}/scan/item", params={"path": path, "target": target})
    context.response = response
    context.item = response.json()

@when("I curl the scan endpoint")
def step_impl(context):
    path = context.env["TEST_SCAN_PATH"]
    cmd = ["curl", "-s", f"{context.base_url}/scan?path={path}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    context.curl_response_raw = result.stdout
    context.curl_response_data = json.loads(result.stdout)

@when("I curl the random file endpoint")
def step_impl(context):
    path = context.env["TEST_SCAN_PATH"]
    target = context.env["TEST_RANDOM_FILE"]
    cmd = ["curl", "-s", f"{context.base_url}/scan/item?path={path}&target={target}"]
    print(f"[Curling Random File] target: {target}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    try:
        context.curl_response_data = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("⚠️  Failed to decode JSON from curl response:")
        print(result.stdout)
        assert False, "Curl response was not valid JSON"

@then("I should receive metadata including path, size, and modified")
def step_impl(context):
    item = context.item
    assert context.response.status_code == 200
    assert "path" in item
    assert "size_bytes" in item
    assert "modified" in item

@then("the curl response should include a list of files")
def step_impl(context):
    assert isinstance(context.curl_response_data, list)
    assert len(context.curl_response_data) > 0

@then("the curl response should include metadata for the file")
def step_impl(context):
    item = context.curl_response_data
    assert "path" in item
    assert "size_bytes" in item
    assert "modified" in item