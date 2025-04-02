import re
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

EXCLUDED_FILES = {'.DS_Store', 'Thumbs.db'}

def extract_exif_datetime(file_path: Path) -> datetime | None:
    try:
        img = Image.open(file_path)
        exif_data = img._getexif()
        if not exif_data:
            return None

        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == "DateTimeOriginal":
                return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception:
        return None

def compute_similarity_score(
    base_file: Path,
    candidate_file: Path,
    exif_times: Dict[Path, datetime],
    size_lookup: Dict[Path, int],
    debug: bool = False
) -> Tuple[int, Dict[str, int]]:
    score = 0
    reasons = {}

    # Absolute name match in different paths
    if base_file.name == candidate_file.name and base_file != candidate_file:
        score += 30
        reasons["exact_name"] = 30

    # Similar name patterns
    base_stem = base_file.stem
    candidate_name = candidate_file.name
    name_variants = [
        rf"{re.escape(base_stem)} copy",
        rf"{re.escape(base_stem)} \(1\)",
        rf"{re.escape(base_stem)}_1",
        rf"{re.escape(base_stem)}-1",
    ]
    for variant in name_variants:
        if re.search(variant, candidate_name, re.IGNORECASE):
            if base_file.parent == candidate_file.parent:
                score += 20
                reasons["similar_name_same_dir"] = 20
            else:
                score += 10
                reasons["similar_name_diff_dir"] = 10
            break

    # Size match
    if size_lookup.get(base_file) == size_lookup.get(candidate_file):
        score += 2
        reasons["same_size"] = 2

    # Time match
    time_a = exif_times.get(base_file)
    time_b = exif_times.get(candidate_file)
    if time_a and time_b:
        try:
            delta = abs((time_a - time_b).total_seconds())
            if delta == 0:
                score += 2
                reasons["same_time"] = 2
            elif delta <= 1:
                score += 1
                reasons["close_time"] = 1
        except Exception:
            pass

    if debug and score > 0:
        print(f"🔍 Score {score}: {base_file.name} ↔ {candidate_file.name} → {reasons}")

    return score, reasons

def build_file_match_queues(root_dir: Path, show_relative_paths: bool = False, debug: bool = False) -> List[Dict]:
    print(f"\n📂 Running file indexer on: {root_dir}")
    all_files = sorted([
        f.resolve() for f in root_dir.rglob("*")
        if f.is_file() and f.name not in EXCLUDED_FILES
    ])
    remaining_files = set(all_files)

    print("📦 Preloading metadata...")
    size_lookup = {f: f.stat().st_size for f in all_files}
    exif_times = {}
    for f in all_files:
        exif_time = extract_exif_datetime(f)
        mtime = datetime.fromtimestamp(f.stat().st_mtime)
        exif_times[f] = exif_time or mtime

    match_clusters: List[Dict] = []

    while remaining_files:
        current = remaining_files.pop()
        cluster = [current]
        reasons: Dict[Path, Dict[str, int]] = {}
        to_remove = set()

        for other in remaining_files:
            score, why = compute_similarity_score(current, other, exif_times, size_lookup, debug)
            if score > 0:
                cluster.append(other)
                to_remove.add(other)
                reasons[other] = why

        remaining_files -= to_remove

        # Skip singletons
        if len(cluster) < 2:
            continue

        # Build explanation
        formatted_why = {
            str(p.relative_to(root_dir)): why for p, why in reasons.items()
        }
        match_clusters.append({
            "files": [str(f.relative_to(root_dir)) for f in cluster],
            "weight": sum(sum(w.values()) for w in reasons.values()),
            "why": formatted_why
        })

    return match_clusters