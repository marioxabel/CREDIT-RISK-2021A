import fire
from .utils import flat_dictionary, display, get_dictionary


class Main:

    @staticmethod
    def hello():
        return "Hello world"

    @staticmethod
    def show(filename: str):
        return display(get_dictionary(filename))

    @staticmethod
    def flatten(filename: str):
        return display(flat_dictionary(get_dictionary(filename)))


#if __name__ == "__main__":
 #   fire.Fire(Main)
