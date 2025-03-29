---
title: SmartMedia Deduplicator – Scan Sequence Flow
version: 0.2.0
last_updated: 2025-03-29
generated_by: Schematicus
source_trigger: Bitwise milestone snapshot
---

```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant API
    participant Scanner
    participant Logger

    User->>CLI: run scan or metadata request
    CLI->>API: call /scan or /scan/item
    API->>Logger: log request event
    API->>Scanner: trigger directory or file scan
    Scanner-->>API: return file metadata
    API->>Logger: log result metadata
    API-->>CLI: return structured JSON result
    CLI-->>User: display scan results
```
