import json
import os
import uuid
from typing import Optional

import matplotlib.pyplot as plt

from .models import Economy
from .settings import (
    WEALTH_DISTR_SIMULATIONS_PATH,
    WEALTH_DISTR_PLOTS_PATH
)


class Main:

    @staticmethod
    def available_simulations():
        base_path = WEALTH_DISTR_SIMULATIONS_PATH
        simulation_files = os.listdir(base_path)
        for file in simulation_files:
            economy = Economy.from_file(file_path=os.path.join(base_path, file))
            description = {
                "key": os.path.basename(file),
                "population": economy.population,
                "epochs": economy.current_epoch,
                "initial-amount": economy.initial_amount,
                "trading-sample": economy.trading_sample,
                "history-length": len(economy.history),
                "stats": economy.get_stats()
            }
            print(json.dumps(description, indent=4))

    @staticmethod
    def _get_economy_from_filename(filename: str):
        base_path = WEALTH_DISTR_SIMULATIONS_PATH
        simulation_file = os.path.join(base_path, filename)
        if not os.path.exists(simulation_file):
            raise ValueError(f"Simulation file not found: {simulation_file}")
        return Economy.from_file(file_path=simulation_file)

    def timeseries(self, key: str, show: bool = False, save: bool = False):
        economy = self._get_economy_from_filename(filename=key)
        figure = economy.plot_timeseries()
        if show:
            plt.show()
        if save:
            random_filename = f"{uuid.uuid4()}.png"
            location = os.path.join(WEALTH_DISTR_PLOTS_PATH, random_filename)
            figure.savefig(location)
            return location

    def histogram(self, key: str, show: bool = False, save: bool = False):
        pass

    @staticmethod
    def simulate(
            population: int,
            epochs: int = 100,
            initial_amount: float = 1000,
            trading_sample: float = 0.5,
            filename: Optional[str] = None
    ):
        if not filename:
            filename = str(uuid.uuid4())
        file_path = os.path.join(WEALTH_DISTR_SIMULATIONS_PATH, filename)
        if os.path.exists(file_path):
            raise ValueError(f"Simulation file already exists: {filename}")
        economy = Economy(
            population=population,
            initial_amount=initial_amount,
            trading_sample=trading_sample,
            include_sessions=True
        )
        economy.epochs(n=epochs)
        economy.save(file_path=file_path)
        return file_path
