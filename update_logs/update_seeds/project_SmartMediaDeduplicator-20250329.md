{
  "SmartMediaDeduplicator_Seed": {
    "project_name": "SmartMedia Deduplicator",
    "description": "A Python-based application to scan, match, and group duplicate or near-duplicate media files (photos/videos) using a weighted, rule-based system with clustering and metadata analysis.",
    "status": "Active",
    "last_updated": "2025-03-29",
    "tech_stack": [
      "Python",
      "FastAPI",
      "Pytest",
      "Behave (BDD)",
      "Pillow (PIL)",
      "dotenv",
      "pathlib",
      "JSON"
    ],
    "features": {
      "Scanning": "Recursive directory scanning for files using configurable root path.",
      "Matching": "Weighted scoring system based on name, size, and metadata time proximity.",
      "Clustering": "Each unique file is compared once; clusters form based on score threshold.",
      "Reporting": "Summary of match types, cluster sizes, and sorted output to JSON.",
      "Env-based Test Harness": ".env config files specify source paths and expected results.",
      "API-first Structure": "Endpoints for scan/match/report operations via FastAPI."
    },
    "key_files": {
      "indexer.py": "Entry point for building match clusters with score aggregation.",
      "matcher.py": "Contains `compute_similarity_score()` with weighted rule logic.",
      "utils.py": "Handles cluster summarization, path cleaning, and JSON safety.",
      "load_test_env.py": "Resolves .env files for setting test paths and output files.",
      "test_indexer.py": "Executes matching and writes both raw and sorted match results."
    },
    "output": {
      "raw": "*_match_queues.json",
      "sorted": "*_match_sorted.json (with weights and match reasons)"
    },
    "match_weights": {
      "Exact Name (diff path)": 30,
      "Similar Name (same path)": 20,
      "Similar Name (diff path)": 10,
      "Size Match": 2,
      "Metadata Time Match (exact)": 2,
      "Metadata Time Match (1s window)": 1
    },
    "workflow_notes": [
      "Files are popped from queue as matched to reduce iteration overhead.",
      "Groupings are sorted by weight, count, then file order.",
      "Unmatched files are excluded from final output.",
      "Current EXIF + mtime timestamp proximity window: 1 second."
    ],
    "next_steps": [
      "Improve `why` trace output with detailed explanation per match.",
      "Add alternate metadata signals (e.g., GPS, camera model) to score.",
      "Refactor cluster sorting to optionally include debug breakdown.",
      "Add CLI control flags for debug, thresholds, and output filtering.",
      "Enable optional hash-based fingerprinting (future)."
    ]
  }
}
