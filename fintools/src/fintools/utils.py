import datetime
import importlib
import functools
import time
import os
import sys
from typing import Generic, TypeVar, Callable

A = TypeVar('A')
B = TypeVar('B')


def compose(this: Callable[..., A], and_then: Callable[[A], B]) -> Callable[..., B]:
    return lambda *x: and_then(this(*x))


def timeit(logger):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            output = func(*args, **kwargs)
            logger.warn("Execution time %s" % (time.time() - start))
            return output
        return wrapper
    return decorator


def get_current_utctime() -> str:
    return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


def streamlit_runner(app_file: str):
    if not os.path.exists(app_file):
        raise ValueError(f"Streamlit app not found: {app_file}")
    streamlit_cli = importlib.import_module("streamlit.cli")
    sys.argv = ["streamlit", "run", app_file]
    streamlit_cli.main()
