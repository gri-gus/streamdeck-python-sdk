from functools import wraps
from threading import Thread
from typing import Callable, Optional


class ThreadingFunc:
    def __init__(
            self,
            func: Callable,
            *,
            daemon: Optional[bool] = None,
    ):
        self.func = func
        self.daemon = daemon

    def __call__(self, *args, **kwargs) -> Thread:
        thread = Thread(target=self.func, args=args, kwargs=kwargs, daemon=self.daemon)
        thread.start()
        return thread


def in_separate_thread(daemon: Optional[bool] = None):
    """
    Decorator for executing the decorated function on a separate thread.

    :param daemon: A daemon thread (True) or not (False). If None, then its initial value is inherited
        from the creating thread.
    """

    def _decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return ThreadingFunc(func=func, daemon=_daemon)(*args, **kwargs)

        return wrapper

    _daemon: Optional[bool] = None
    if callable(daemon):
        return _decorator(func=daemon)
    _daemon = daemon
    return _decorator
