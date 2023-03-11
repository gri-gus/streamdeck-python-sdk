import logging
from functools import wraps
from logging.handlers import RotatingFileHandler
from pathlib import Path

from decohints import decohints

logger: logging.Logger = logging.getLogger('default')


def init_logger(debug: bool, log_file: Path) -> None:
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    # create file handler which logs even debug messages
    rfh = RotatingFileHandler(
        log_file,
        mode='a',
        maxBytes=3 * 1024 * 1024,
        backupCount=2,
        encoding="utf-8",
        delay=False
    )
    # fh = logging.FileHandler(log_file)
    rfh.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d): %(message)s"
    )
    rfh.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(rfh)


@decohints
def log_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except BaseException as err:
            logger.error(str(err), exc_info=True)
            return
        return result

    return wrapper
