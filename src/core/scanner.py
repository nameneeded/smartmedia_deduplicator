from pathlib import Path
from typing import Generator, Optional

SUPPORTED_IMAGE_EXT = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
SUPPORTED_VIDEO_EXT = {'.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv'}
EXCLUDED_FILES = {".DS_Store", "Thumbs.db", "desktop.ini"}

def walk_directory(path: Path) -> Generator[Path, None, None]:
    for p in path.rglob('*'):
        if p.name in EXCLUDED_FILES:
            continue
        if p.is_file():
            yield p

def classify_filetype(path: Path) -> Optional[str]:
    ext = path.suffix.lower()
    if ext in SUPPORTED_IMAGE_EXT:
        return "image"
    elif ext in SUPPORTED_VIDEO_EXT:
        return "video"
    return None