import logging
import os
from pathlib import Path

PLUGIN_LOGS_DIR_PATH: Path = Path(os.environ.get("PLUGIN_LOGS_DIR_PATH", Path(__file__).parents[2] / "logs"))
PLUGIN_NAME: str = os.environ.get("PLUGIN_NAME", Path(__file__).parents[1].name)
LOG_FILE_PATH: Path = PLUGIN_LOGS_DIR_PATH / Path(f"{PLUGIN_NAME}.log")
LOG_LEVEL: int = logging.DEBUG
