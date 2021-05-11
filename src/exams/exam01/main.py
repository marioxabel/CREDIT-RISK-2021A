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
