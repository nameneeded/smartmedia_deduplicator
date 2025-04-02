from pathlib import Path
import json
import sys

# Add project root to path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.core.indexer import build_file_match_queues
from src.utils.load_test_env import load_test_env

def main():
    env = load_test_env()
    scan_path = Path(env["TEST_SCAN_PATH"])
    output_file_raw = Path(env["TEST_MATCH_FILE"])

    # Compute sorted output file path
    output_file_sorted = output_file_raw.with_name(
        output_file_raw.stem.replace("_match_queues", "_match_sorted") + ".json"
    )

    print(f"\n📁 Scanning path: {scan_path}")
    match_results = build_file_match_queues(scan_path, show_relative_paths=True)

    # Only include clusters with more than 1 file
    clusters = [group["files"] for group in match_results if len(group["files"]) > 1]
    sorted_clusters = sorted(match_results, key=lambda g: (-g["weight"], -len(g["files"]), g["files"][0]))
    for idx, group in enumerate(sorted_clusters):
        group["index"] = idx
    sorted_clusters = [group for group in sorted_clusters if len(group["files"]) > 1]

    # Write raw output
    output_file_raw.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file_raw, "w") as f:
        json.dump(clusters, f, indent=2)

    # Write sorted output (with weights and reasons)
    with open(output_file_sorted, "w") as f:
        json.dump(sorted_clusters, f, indent=2)

    # Summary
    print(f"\n✅ Match clusters written to: {output_file_raw.name}")
    print(f"📥 Sorted clusters written to: {output_file_sorted.name}")
    print(f"🔢 Total clusters: {len(clusters)}")

if __name__ == "__main__":
    main()
