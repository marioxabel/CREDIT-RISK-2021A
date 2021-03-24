from typing import List

from fintools.settings import get_logger
from fintools.utils import timeit

logger = get_logger(name=__name__)


class Main:

    def __init__(self):
        logger.info("Main object initialized.")

    def element(self, position: int) -> int:
        pass

    @timeit(logger=logger)
    def sequence(self, length: int) -> List[int]:
        pass
