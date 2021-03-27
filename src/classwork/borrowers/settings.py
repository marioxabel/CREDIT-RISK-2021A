import os


BORROWERS_BASE_PATH = os.path.dirname(os.path.abspath(__file__))
BORROWERS_FILENAME = os.environ.get("BORROWERS_FILENAME", default="candidates.json")
BORROWERS_FILEPATH = os.path.join(BORROWERS_BASE_PATH, BORROWERS_FILENAME)
