from typing import List

from fintools.settings import get_logger
from fintools.utils import timeit

logger = get_logger(name=__name__)


class Main:

    def __init__(self):
        logger.info("Main object initialized.")

    @method_caching
    def element(self, position: int) -> int:
        n1, n2 = 0, 1
        count = 0

        # check if the number of terms is valid
        if position <= 0:
            print("Please enter a positive integer")
        elif position == 1:
            print("Fibonacci sequence upto", position, ":")
            print(n1)
        else:
            print("Fibonacci sequence:")
            while count < position:
                nth = n1 + n2
                # update values
                n1 = n2
                n2 = nth
                count += 1
        print(n1)

    @timeit
    def sequence(self, length: int) -> int:
        pass
