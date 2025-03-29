from pathlib import Path
from typing import List, Optional
from datetime import datetime
from src.api.models.file_record import FileRecord
from src.core.scanner import walk_directory, classify_filetype

def scan_directory(path: Path) -> List[FileRecord]:
    records = []
    for file_path in walk_directory(path):
        ftype = classify_filetype(file_path)
        if not ftype:
            continue
        stat = file_path.stat()
        records.append(FileRecord(
            path=str(file_path.resolve()),
            size_bytes=stat.st_size,
            modified=datetime.fromtimestamp(stat.st_mtime),
            type=ftype
        ))
    return records

def get_single_file_record(target_path: Path, base_path: Path) -> Optional[FileRecord]:
    from src.core.scanner import classify_filetype

    if not target_path.exists() or not target_path.is_file():
        return None
    if base_path not in target_path.parents:
        return None

    ftype = classify_filetype(target_path)
    if not ftype:
        return None

    stat = target_path.stat()
    return FileRecord(
        path=str(target_path.resolve()),
        size_bytes=stat.st_size,
        modified=datetime.fromtimestamp(stat.st_mtime),
        type=ftype
    )