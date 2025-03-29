import json
import os
import requests
from behave import given, when, then
from urllib.parse import urlencode

BASELINE_PATH = "tests/resources/pictures_scan_baseline.json"
API_BASE_URL = "http://127.0.0.1:8000"
SCAN_PATH = "/Users/jseanw/Desktop/Pictures"

def safe_url(endpoint, params):
    return f"{API_BASE_URL}{endpoint}?{urlencode(params)}"

@given("a baseline dataset of scanned files is available")
def step_impl_given_baseline_loaded(context):
    with open(BASELINE_PATH, "r") as f:
        context.baseline = json.load(f)

@given("the scan path is \"{scan_path}\"")
def step_impl_given_scan_path(context, scan_path):
    context.scan_path = scan_path

@given("I select a known file from the baseline")
def step_impl_given_sample_file(context):
    context.sample_file = context.baseline[0]

@when("I request a scan of the entire directory")
def step_impl_when_full_scan(context):
    url = safe_url("/scan", {"path": context.scan_path})
    context.response = requests.get(url)

@when("I request metadata for that specific file")
@when("I request metadata for a file that does not exist")
def step_impl_when_file_metadata(context):
    if hasattr(context, "sample_file"):
        target_path = context.sample_file["path"]
    else:
        target_path = os.path.join(context.scan_path, "nonexistent_file.jpg")
    url = safe_url("/scan/item", {"path": context.scan_path, "target": target_path})
    context.response = requests.get(url)

@then("the API should return the same number of files as in the baseline")
def step_impl_then_count_matches(context):
    assert context.response.status_code == 200
    data = context.response.json()
    assert len(data) == len(context.baseline)

@then("the API should return the correct metadata for the file")
def step_impl_then_metadata_matches(context):
    assert context.response.status_code == 200
    result = context.response.json()
    for key in ("path", "size_bytes", "type"):
        assert result[key] == context.sample_file[key]
    assert context.sample_file["modified"][:19] in result["modified"]

@then("the API should return a 404 error")
def step_impl_then_404(context):
    assert context.response.status_code == 404
