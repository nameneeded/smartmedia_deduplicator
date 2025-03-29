import os
import json
from pathlib import Path
from datetime import datetime

OUTPUT_PATH = Path("tests/resources/pictures_scan_baseline.json")
TARGET_DIR = Path("/Users/jseanw/Desktop/Pictures")

SUPPORTED_IMAGE_EXT = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
SUPPORTED_VIDEO_EXT = {'.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv'}
EXCLUDED_FILES = {".DS_Store", "Thumbs.db", "desktop.ini"}

def classify_filetype(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in SUPPORTED_IMAGE_EXT:
        return "image"
    elif ext in SUPPORTED_VIDEO_EXT:
        return "video"
    return "other"

def record_directory_listing():
    records = []
    print(f"Scanning Directory: {TARGET_DIR.resolve()}")
    for file_path in TARGET_DIR.rglob('*'):
        if file_path.is_file():
            print(f"Found file: {file_path}")
            ftype = classify_filetype(file_path)
            stat = file_path.stat()
            if file_path.name in EXCLUDED_FILES:
                continue
            records.append({
                "path": str(file_path.resolve()),
                "size_bytes": stat.st_size,
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "type": ftype
            })
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(records, f, indent=2)
    print(f"Wrote baseline data for {len(records)} files to {OUTPUT_PATH}")

if __name__ == "__main__":
    record_directory_listing()
