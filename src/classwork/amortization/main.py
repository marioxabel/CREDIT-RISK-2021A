import json
import hashlib
import os

from .settings import (
    AMORTIZATION_BASE_PATH,
    AMORTIZATION_CONFIG_DIRPATH,
    AMORTIZATION_TABLE_DIRPATH
)

from fintools import Amortization
from fintools.utils import streamlit_runner


class Main:

    @staticmethod
    def hello(world: str):
        print(f"Hello {world}")

    @staticmethod
    def setup():
        if not os.path.exists(AMORTIZATION_TABLE_DIRPATH):
            os.makedirs(AMORTIZATION_TABLE_DIRPATH)
        if not os.path.exists(AMORTIZATION_CONFIG_DIRPATH):
            os.makedirs(AMORTIZATION_CONFIG_DIRPATH)

    @staticmethod
    def explorer():
        explorer_path = os.path.join(AMORTIZATION_BASE_PATH, "streamlit_explorer.py")
        streamlit_runner(app_file=explorer_path)

    def table(self, amount: float, n: int, rate: float, show: bool = False, save: bool = False):
        self.setup()
        amortization = Amortization(amount=amount, rate=rate, n=n)
        config = amortization.to_dict()
        config_id = hashlib.md5(json.dumps(config).encode()).hexdigest()
        table = amortization.get_table()
        if save:
            # Save config
            config_path = os.path.join(AMORTIZATION_CONFIG_DIRPATH, config_id + ".json")
            with open(config_path, "w") as file:
                file.write(json.dumps(config))
            # Save table
            table_path = os.path.join(AMORTIZATION_TABLE_DIRPATH, config_id + ".csv")
            table.to_csv(table_path, index=False)
        if show:
            print(table.to_string())
