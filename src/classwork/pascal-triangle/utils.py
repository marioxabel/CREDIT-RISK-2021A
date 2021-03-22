import functools
import time


def timeit():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            output = func(*args, **kwargs)
            print("Execution time %s" % (time.time() - start))
            return output
        return wrapper
    return decorator


def caching(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = hash(frozenset(list(args) + list(kwargs.items())))
        if key in cache:
            return cache[key]
        cache[key] = func(*args, **kwargs)
        return wrapper(*args, **kwargs)
    return wrapper
