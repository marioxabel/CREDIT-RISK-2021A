from .utils import timeit, caching
from .triangle_builder import TriangleBuilder


class Main:

    def __init__(self):
        self.builder = TriangleBuilder()

    @staticmethod
    def hello():
        return "Hello, world!"

    @caching
    def get_element(self, i: int, j: int) -> int:
        return 1 if (j == 0 or j >= i) else \
            self.get_element(i=i-1, j=j) + self.get_element(i=i-1, j=j-1)

    def naive(self, level: int, index: int = 0) -> None:
        if index < level:
            row = [self.get_element(i=index, j=j) for j in range(index+1)]
            print(*row, sep=" ")
            self.naive(level=level, index=index+1)

    def optimized(self, level: int, index: int = 0) -> None:
        if index < level:
            row = self.builder.get_row(index=index)
            print(*row, sep=" ")
            self.optimized(level=level, index=index + 1)

    @timeit()
    def pascal_triangle(self, level: int, start: int = 0, method: str = "naive"):
        if method.lower() == "naive":
            self.naive(level=level, index=start)
        elif method.lower() == "optimized":
            self.optimized(level=level, index=start)
