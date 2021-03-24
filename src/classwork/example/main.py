
class Main:

    @staticmethod
    def hello(name: str = "world"):
        return f"Hello, {name}!"

    @staticmethod
    def reverse(string: str):
        return string[::-1]