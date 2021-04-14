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


def flat_dictionary(input_dict, separator='.', prefix=''):
    output_dict = {}
    for key, value in input_dict.items():
        if isinstance(value, dict) and value:
            deeper = flat_dictionary(value, separator, prefix+key+separator)
            output_dict.update({key2: val2 for key2, val2 in deeper.items()})
        elif isinstance(value, list) and value:
            for index, sublist in enumerate(value, start=0):
                if isinstance(sublist, dict) and sublist:
                    deeper = flat_dictionary(sublist, separator, prefix+key+separator+str(index)+separator)
                    output_dict.update({key2: val2 for key2, val2 in deeper.items()})
                else:
                    output_dict[prefix+key+separator+str(index)] = value
        else:
            output_dict[prefix+key] = value
    return output_dict
