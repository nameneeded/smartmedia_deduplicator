import os
import logging
import logging.config
import yaml

CONFIG_PATH = "src/logging/logging_config.yaml"
LOG_FILE_PATH = "logs/app.log"


def force_log_rotation():
    logger = logging.getLogger()
    for handler in logger.handlers:
        if isinstance(handler, logging.handlers.RotatingFileHandler):
            handler.doRollover()
            print("🔁 Log rotation triggered manually.")
            return
    print("⚠️ No rotating file handler found. Check logging configuration.")


def main():
    if not os.path.exists(CONFIG_PATH):
        print(f"⚠️ Logging config not found at {CONFIG_PATH}")
        return

    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)

    force_log_rotation()


if __name__ == "__main__":
    main()