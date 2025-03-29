import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

def setup_logging(log_file: str, level: str = "INFO", when: str = "midnight", backup_count: int = 7):
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    handler = TimedRotatingFileHandler(log_file, when=when, backupCount=backup_count)
    formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
    handler.setFormatter(formatter)

    logging.basicConfig(level=getattr(logging, level.upper()), handlers=[handler])