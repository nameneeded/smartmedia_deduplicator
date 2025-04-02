from pathlib import Path
import json
from typing import List, Dict, Literal, Optional

ReviewDecision = Literal["keep", "delete", "merge", "uncertain"]

NOISE_FILES = {'.DS_Store'}

def load_clusters(file_path: Path) -> List[Dict]:
    """Load clustered match data from a sorted match JSON file."""
    with file_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_review_state(
    reviewed_clusters: List[Dict], output_path: Path
) -> None:
    """Save reviewed clusters with human decisions."""
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(reviewed_clusters, f, indent=2, ensure_ascii=False)


def add_decision_to_cluster(
    cluster: Dict,
    decision: Optional[ReviewDecision] = None,
    reviewer: Optional[str] = None,
    notes: Optional[str] = None,
    rotation_map: Optional[Dict[str, int]] = None,
) -> Dict:
    """Tag a cluster with per-image decisions, optional rotation, and summary review metadata."""
    # Apply rotation and per-image decisions
    if rotation_map:
        for f in cluster.get("files", []):
            if isinstance(f, dict):
                f_path = f.get("path", "")
                f["rotation"] = rotation_map.get(f_path, 0)

    # Derive summary decision from per-image votes
    decisions = {f.get("decision", "uncertain") for f in cluster["files"]}

    if len(decisions) == 1:
        summary = list(decisions)[0]
    elif decisions == {"keep", "delete"}:
        summary = "dedup"
    else:
        summary = "mixed"

    cluster["review"] = {
        "summary": summary,
        "reviewer": reviewer,
        "notes": notes,
    }
    return cluster


def filter_clusters_for_review(clusters: List[Dict]) -> List[Dict]:
    return [c for c in clusters if "review" not in c or c.get("review", {}).get("summary") == "uncertain"]

def normalize_cluster_paths(clusters: List[Dict], base_dir: Path) -> List[Dict]:
    """Update file paths to absolute paths and convert to dict format for review UI."""
    for cluster in clusters:
        updated_files = []
        for f in cluster.get("files", []):
            if isinstance(f, str) and Path(f).name in NOISE_FILES:
                continue  # Skip system clutter like .DS_Store
            full_path = (base_dir / f).resolve()
            updated_files.append({"path": str(full_path), "name": Path(f).name})
        cluster["files"] = updated_files
    return clusters

def merge_review_data(
    base_clusters: List[Dict],
    reviewed_clusters: List[Dict]
) -> List[Dict]:
    """Merge full reviewed clusters into base list using 'index'."""
    reviewed_by_index = {
        c["index"]: c for c in reviewed_clusters if "review" in c
    }

    for i, cluster in enumerate(base_clusters):
        idx = cluster.get("index", i)
        if idx in reviewed_by_index:
            base_clusters[i] = reviewed_by_index[idx]

    return base_clusters