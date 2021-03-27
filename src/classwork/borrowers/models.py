import os
import json
from typing import Any, Dict, Optional

from fintools.utils import get_current_utctime

from .settings import BORROWERS_FILEPATH


class Borrower:

    def __init__(self, email: str, age: int, income: float, created_at: Optional = None, updated_at: Optional = None):
        self.email = email
        self.age = age
        self.income = income
        self.created_at = created_at or get_current_utctime()
        self.updated_at = updated_at or self.created_at

    @staticmethod
    def get(email: str) -> Optional['Borrower']:
        candidates = Borrower.get_candidates()
        for candidate in candidates["candidates"]:
            if candidate["email"] == email:
                return Borrower(**candidate)

    def update_filed(self, field_name: str, field_value: Any):
        self.updated_at = get_current_utctime()
        setattr(self, field_name, field_value)

    def to_dict(self) -> Dict:
        return {
            "email": self.email,
            "age": self.age,
            "income": self.income,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @staticmethod
    def get_candidates():
        if not os.path.exists(BORROWERS_FILEPATH):
            raise ValueError(f"File does not exists: {BORROWERS_FILEPATH}")
        with open(BORROWERS_FILEPATH, "r") as file:
            candidates_content = file.read()  # This returns a string
        candidates = json.loads(candidates_content)  # This returns a dictionary
        return candidates

    def save(self):
        # 1. Open the file (candidates.json) and load the content
        candidates = self.get_candidates()
        # 2. Verify if email already exists
        emails = [candidate["email"] for candidate in candidates["candidates"]]
        if self.email in emails:
            return self.update()
        # 3. Add new borrower to the candidates.json file
        candidates["candidates"].append(self.to_dict())
        candidates["last_updated"] = get_current_utctime()
        candidates_content_new = json.dumps(candidates, indent=4)
        # 4. Save the new json file
        with open(BORROWERS_FILEPATH, "w") as file:
            file.write(candidates_content_new)

    def update(self):
        # 1. Open the file (candidates.json) and load the content
        candidates = self.get_candidates()
        # 2. Verify if email exists
        emails = [candidate["email"] for candidate in candidates["candidates"]]
        if self.email not in emails:
            return self.save()
        # 3. Update candidates
        candidate_list = [
            candidate if self.email != candidate["email"] else self.to_dict()
            for candidate in candidates["candidates"]
        ]
        candidates["candidates"] = candidate_list
        candidates["last_updated"] = get_current_utctime()
        candidates_content_new = json.dumps(candidates, indent=4)
        # 4. Save the new json file
        with open(BORROWERS_FILEPATH, "w") as file:
            file.write(candidates_content_new)
