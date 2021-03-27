import json
from typing import Any

from fintools.utils import get_current_utctime

from .settings import *
from .models import Borrower


class Main:

    @staticmethod
    def setup(replace: bool = False):
        if os.path.exists(BORROWERS_FILEPATH) and not replace:
            return f"File already exists: {BORROWERS_FILEPATH}"
        initial_layout = {
            "last_updated": get_current_utctime(),
            "candidates": []
        }
        content = json.dumps(initial_layout, indent=4)
        with open(BORROWERS_FILEPATH, "w") as file:
            file.write(content)
        return f"File created: {BORROWERS_FILEPATH}"

    def register(self, email: str, age: int, income: float):
        self.setup()
        new_borrower = Borrower(email=email, age=age, income=income)
        new_borrower.save()

    def update(self, email: str, field_name: str, field_value: Any):
        self.setup()
        borrower = Borrower.get(email=email)
        if borrower is None:
            return f"Borrower {email} not found."
        borrower.update_filed(field_name=field_name, field_value=field_value)
        borrower.update()

    @staticmethod
    def show():
        with open(BORROWERS_FILEPATH, "r") as file:
            content = file.read()
        # Optional: transform to dictionary
        candidates = json.loads(content)
        # Return the dictionary as a string
        return json.dumps(candidates, indent=4)
