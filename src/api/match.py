from fastapi import APIRouter
from pathlib import Path
from src.core.indexer import build_file_match_queues #, name_matching, size_matching, meta_matching
from src.utils.load_test_env import load_test_env

router = APIRouter()

@router.get("/match")
def get_match_clusters():
    env = load_test_env()
    scan_path = Path(env["TEST_SCAN_PATH"])
    
    clusters = build_file_match_queues(scan_path)

    # Calculate summary info
    summary = {
        "name_match": 0,
        "size_match": 0,
        "meta_match": 0,
        "total_clusters": len(clusters)
    }

    # Reload all match details to compute summary
    all_files = list(scan_path.rglob("*"))
    filenames = [f.name for f in all_files if f.is_file()]
    file_lookup = {f.name: f for f in all_files if f.is_file()}

    for filename in filenames:
        if name_matching(filename, filenames):
            summary["name_match"] += 1
        if size_matching(file_lookup[filename], all_files):
            summary["size_match"] += 1

    meta = meta_matching(all_files)
    summary["meta_match"] = len(meta)

    return {
        "clusters": clusters,
        "summary": summary
    }