from typing import Dict, List, Optional


def corner_case(func):
    def wrapper(self, i, j, *args, **kwargs):
        if j >= i or j == 0:
            return 1
        return func(self, i=i, j=j, *args, **kwargs)
    return wrapper


def lambda_wrapper(value):
    return lambda: value


class TriangleBuilder:

    def __init__(self, cache: Optional[Dict] = None):
        self.cache = cache if cache is not None else {}

    def save(self, i: int, j: int, value: int) -> int:
        key = (i, j)
        self.cache[key] = lambda_wrapper(value)
        return value

    @corner_case
    def get(self, i: int, j: int, default=None) -> int:
        key = (i, j)
        return self.cache.get(key, default)()

    @corner_case
    def create(self, i: int, j: int) -> int:
        upper_left = self.get_or_create(i=i-1, j=j-1)
        upper_center = self.get_or_create(i=i-1, j=j)
        return self.save(i=i, j=j, value=upper_left+upper_center)

    def get_or_create(self, i: int, j: int) -> int:
        return self.get(i, j, default=lambda: self.create(i, j))

    def get_row(self, index: int) -> List[int]:
        return [self.get_or_create(i=index, j=j) for j in range(index+1)]
