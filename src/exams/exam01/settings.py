import os


# Base path
FLATTEN_BASE_PATH = os.environ.get(
    "FLATTEN_BASE_PATH",
    default=os.path.dirname(os.path.abspath(__file__))
)
# Simulations
FLATTEN_FILES_DIRECTORY = os.environ.get(
    "FLATTEN_FILES_DIRECTORY",
    default="json-files"
)
FLATTEN_FILES_PATH = os.path.join(FLATTEN_BASE_PATH, FLATTEN_FILES_DIRECTORY)
