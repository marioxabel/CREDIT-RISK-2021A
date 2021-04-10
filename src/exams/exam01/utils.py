import json
import os
from typing import Dict

from .settings import FLATTEN_FILES_PATH


def get_file_path(filename: str):
    file_path = os.path.join(FLATTEN_FILES_PATH, filename)
    if not os.path.exists(file_path):
        raise ValueError(f"File not found: {file_path}")
    return file_path


def get_dictionary(filename: str) -> Dict:
    file_path = get_file_path(filename=filename)
    with open(file_path, "r") as file:
        content = file.read()
    dictionary = json.loads(content)
    return dictionary


def display(target: Dict):
    print(json.dumps(target, indent=4))


def flat_dictionary(target):
    pass
