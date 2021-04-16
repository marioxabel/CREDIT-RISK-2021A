import os

# Application's base path
AMORTIZATION_BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Space to save amortization tables (csv)
AMORTIZATION_TABLE_DIRNAME = os.environ.get("AMORTIZATION_TABLE_DIRNAME", default="tables")
AMORTIZATION_TABLE_DIRPATH = os.path.join(AMORTIZATION_BASE_PATH, AMORTIZATION_TABLE_DIRNAME)

# Space to save amortization configuration (json)
AMORTIZATION_CONFIG_DIRNAME = os.environ.get("AMORTIZATION_CONFIG_DIRNAME", default="configs")
AMORTIZATION_CONFIG_DIRPATH = os.path.join(AMORTIZATION_BASE_PATH, AMORTIZATION_CONFIG_DIRNAME)
