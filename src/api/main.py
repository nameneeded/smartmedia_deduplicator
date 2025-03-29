from fastapi import FastAPI, Query, HTTPException
from pathlib import Path
from typing import List, Optional
from src.api.models.file_record import FileRecord
from src.api.routes.scan import scan_directory, get_single_file_record
from src.logging.setup_logging import setup_logging
import logging

setup_logging("logs/app.log")
logger = logging.getLogger(__name__)

app = FastAPI(title="SmartMedia Deduplicator API")

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