# 🧪 Testing Guide for `tests/`

This folder contains both traditional `pytest` tests and `behave` feature-based tests.

---

## ✅ Pytest

Run a specific file:
```bash
pytest tests/test_scan_api.py -v
```

Run all tests:
```bash
pytest -v
```

---

## ✅ Behave (BDD-style)

Run all Gherkin tests:
```bash
behave
```

Feature files live in:
```
tests/features/*.feature
```

Step implementations live in:
```
tests/features/steps/
```

---

## 🧪 Manual API Testing with `curl`

### 🎯 Get Full Scan:
```bash
curl "http://127.0.0.1:8000/scan?path=/Users/jseanw/Desktop/Pictures" | jq
```

### 🎯 Get Specific File:
```bash
curl "http://127.0.0.1:8000/scan/item?path=/Users/jseanw/Desktop/Pictures&target=/Users/jseanw/Desktop/Pictures/202301/20230102_114610.jpg" | jq
```

Or use this safe format with URL encoding:
```bash
curl --get \
  --data-urlencode "path=/Users/jseanw/Desktop/Pictures" \
  --data-urlencode "target=/Users/jseanw/Desktop/Pictures/202301/20230102_114610.jpg" \
  http://127.0.0.1:8000/scan/item | jq
```

You should see metadata like:
```json
{
  "path": "/Users/jseanw/Desktop/Pictures/202301/20230102_114610.jpg",
  "size_bytes": 3032485,
  "modified": "2023-01-02T11:46:13",
  "type": "image"
}
```

404s or "not supported" mean the file is either missing, outside scope, or filtered.
