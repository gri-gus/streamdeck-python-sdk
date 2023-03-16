import logging
from functools import wraps
from logging.handlers import RotatingFileHandler
from pathlib import Path

from decohints import decohints

logger: logging.Logger = logging.getLogger('default')


def init_logger(log_file: Path, log_level: int = logging.DEBUG) -> None:
    logger.setLevel(log_level)
    logs_dir: Path = log_file.parent
    logs_dir.mkdir(parents=True, exist_ok=True)
    rfh = RotatingFileHandler(
        log_file,
        mode='a',
        maxBytes=3 * 1024 * 1024,
        backupCount=2,
        encoding="utf-8",
        delay=False,
    )
    rfh.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d): %(message)s"
    )
    rfh.setFormatter(formatter)
    logger.addHandler(rfh)


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
            logger.error(str(err), exc_info=True)
            return
        return result

    return wrapper
