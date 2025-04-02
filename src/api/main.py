from fastapi import FastAPI, Query, HTTPException
from pathlib import Path
from typing import List, Optional
from src.api.models.file_record import FileRecord
from src.api.routes.scan import scan_directory, get_single_file_record
from src.logging.setup_logging import setup_logging
from src.core.indexer import build_file_match_queues
from src.api import match

import logging

setup_logging("logs/app.log")
logger = logging.getLogger(__name__)

app = FastAPI(title="SmartMedia Deduplicator API")
app.include_router(match.router)

@app.get("/scan", response_model=List[FileRecord])
def scan(path: str = Query(..., description="Path to directory to scan")):
    logger.info(f"Scanning path: {path}")
    return scan_directory(Path(path))

@app.get("/scan/item", response_model=FileRecord)
def scan_item(
    path: str = Query(..., description="Base directory path to scan"),
    target: str = Query(..., description="Full path to file to retrieve")
):
    logger.info(f"Requesting metadata for file: {target}")
    result = get_single_file_record(Path(target), Path(path))
    if result is None:
        raise HTTPException(status_code=404, detail="File not found or not supported")
    return result

@app.get("/index", summary="Index media files by potential duplicates", description="Uses filename and file size heuristics to queue candidate duplicate files for later deduplication.")
def index_match_queues(path: str):
    scan_path = Path(path).expanduser()
    if not scan_path.exists() or not scan_path.is_dir():
        raise HTTPException(status_code=400, detail="Provided path is invalid or does not exist")

    queues = build_file_match_queues(scan_path)
    return queues