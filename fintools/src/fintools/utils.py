import datetime
import functools
import time
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
