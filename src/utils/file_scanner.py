from typing import List, Dict, Generator
from pathlib import Path
from datetime import datetime
import mimetypes

EXCLUDED_FILES = {".DS_Store", "Thumbs.db"}

def classify_filetype(path: Path) -> str:
    mime_type, _ = mimetypes.guess_type(str(path))
    if mime_type:
        if mime_type.startswith("image"):
            return "image"
        elif mime_type.startswith("video"):
            return "video"
    return "other"

def scan_directory(path: Path) -> List[Dict]:
    def walk_directory(p: Path) -> Generator[Path, None, None]:
        for item in p.rglob("*"):
            if item.is_file() and item.name not in EXCLUDED_FILES:
                yield item

    return [
        {
            "path": str(p.resolve()),
            "size_bytes": p.stat().st_size,
            "modified": datetime.fromtimestamp(p.stat().st_mtime).isoformat(),
            "type": classify_filetype(p),
        }
        for p in walk_directory(path)
    ]