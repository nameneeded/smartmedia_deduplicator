# src/core/indexer.py
from pathlib import Path
from typing import List, Dict
from .matcher import extract_exif_datetime, compute_similarity_score
from .utils import summarize_clusters, clean_cluster_output

def build_file_match_queues(
    root_dir: Path,
    show_relative_paths: bool = False,
    debug: bool = False
) -> List[Dict]:
    print(f"\n📂 Running file indexer on: {root_dir}")
    all_files = sorted([f.resolve() for f in root_dir.rglob("*") if f.is_file()])
    remaining_files = set(all_files)

    # Preload metadata
    print("📦 Preloading metadata...")
    size_lookup = {f: f.stat().st_size for f in all_files}
    exif_times = {f: extract_exif_datetime(f) or f.stat().st_mtime for f in all_files}

    match_clusters = []

    while remaining_files:
        current = remaining_files.pop()
        cluster = [current]
        reasons = {}
        total_weight = 0
        to_remove = set()

        for other in remaining_files:
            score, why = compute_similarity_score(current, other, exif_times, size_lookup, debug)
            if score > 0:
                cluster.append(other)
                to_remove.add(other)
                total_weight += score
                reasons.setdefault(current, {})[other] = why

        remaining_files -= to_remove
        match_clusters.append({
            "files": cluster,
            "weight": total_weight,
            "reasons": reasons
        })

    cleaned = clean_cluster_output(match_clusters, root_dir, show_relative_paths)
    summarize_clusters(cleaned)
    return cleaned
