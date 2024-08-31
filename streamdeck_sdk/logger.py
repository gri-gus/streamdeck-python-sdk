import logging
from functools import wraps
from logging.handlers import RotatingFileHandler
from pathlib import Path

from decohints import decohints

_root_logger: logging.Logger = logging.getLogger()
_log_errors_decorator_logger = logging.getLogger("log_errors_decorator")
logger = logging.getLogger("streamdeck_plugin")


def init_root_logger(
        log_file: Path,
        log_level: int = logging.DEBUG,
        log_max_bytes: int = 3 * 1024 * 1024,
        log_backup_count: int = 2,
) -> None:
    _root_logger.setLevel(log_level)
    logs_dir: Path = log_file.parent
    logs_dir.mkdir(parents=True, exist_ok=True)
    rfh = RotatingFileHandler(
        log_file,
        mode='a',
        maxBytes=log_max_bytes,
        backupCount=log_backup_count,
        encoding="utf-8",
        delay=False,
    )
    rfh.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d): %(message)s"
    )
    rfh.setFormatter(formatter)
    _root_logger.addHandler(rfh)


@decohints
def log_errors(func):
    """
    A decorator that logs and suppresses errors in the function being decorated.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except BaseException as err:
            _log_errors_decorator_logger.error(str(err), exc_info=True)
            return
        return result

    return wrapper


def rename_plugin_logger(name: str):
    logger.name = name
