from typing import Optional


class Main:

    @staticmethod
    def hello(name: Optional[str] = None) -> str:
        if name is None:
            name = "world"
        return f"Hello, {name}!"
