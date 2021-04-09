import itertools
import random
import json
import os

import pandas as pd
from matplotlib.figure import Figure

from typing import Dict, List, Optional

from .agent import Agent
from ..settings import (
    WEALTH_DISTR_DEFAULT_HIST_PLOT_KWARGS,
    WEALTH_DISTR_DEFAULT_LINE_PLOT_KWARGS
)


class Economy:
    SOURCE_EPOCH = "epoch"
    SOURCE_SESSION = "session"

    def __init__(
            self,
            population: int,
            initial_amount: float,
            trading_sample: float,
            sessions_per_epoch: int = 100,
            disable_epoch_history: bool = False,
            include_sessions: bool = False,
            agents: Optional[List[Agent]] = None,
            history: Optional[List[Dict]] = None,
            current_epoch: int = 0,
    ):
        self.sessions_per_epoch = sessions_per_epoch
        self.initial_amount = initial_amount
        self.trading_sample = trading_sample
        self.population = population
        self.agents = [
            Agent(money=self.initial_amount)
            for _ in range(population)
        ] if not agents else agents
        self.current_epoch = current_epoch
        self.include_sessions = include_sessions
        self.disable_epoch_history = disable_epoch_history
        self.history = history or []
        self._snapshot(source=self.SOURCE_EPOCH)
        if include_sessions:
            self._snapshot(source=self.SOURCE_SESSION)

    @staticmethod
    def from_json(content: str) -> 'Economy':
        dictionary = json.loads(content)
        dictionary["agents"] = [
            Agent(**agent_dictionary)
            for agent_dictionary in dictionary.get("agents", [])
        ]
        return Economy(**dictionary)

    @staticmethod
    def from_file(file_path: str) -> 'Economy':
        if not os.path.exists(file_path):
            raise ValueError(f"Path does not exists: {file_path}")
        with open(file_path, "r") as file:
            content = file.read()
        return Economy.from_json(content)

    def to_dict(self) -> Dict:
        return {
            "population": self.population,
            "initial_amount": self.initial_amount,
            "trading_sample": self.trading_sample,
            "sessions_per_epoch": self.sessions_per_epoch,
            "disable_epoch_history": self.disable_epoch_history,
            "include_sessions": self.include_sessions,
            "agents": [agent.to_dict() for agent in self.agents],
            "history": self.history,
            "current_epoch": self.current_epoch
        }

    def save(self, file_path: str):
        content = json.dumps(self.to_dict(), indent=4)
        with open(file_path, "w") as file:
            file.write(content)

    def _snapshot(self, source: str):
        if source == self.SOURCE_SESSION and not self.include_sessions:
            return
        elif source == self.SOURCE_EPOCH and self.disable_epoch_history:
            return
        summary = {
            "source": source,
            **self.get_stats()
        }
        self.history.append(summary)

    def get_data(self) -> pd.DataFrame:
        return pd.DataFrame([agent.to_dict() for agent in self.agents])

    def get_stats(self):
        return self.get_data().money.describe().to_dict()

    def epoch(self):
        self.current_epoch += 1
        for _ in range(self.sessions_per_epoch):
            self._trading_session()
        self._snapshot(source=self.SOURCE_EPOCH)

    def epochs(self, n: int):
        for _ in range(n):
            self.epoch()

    def _trading_session(self):
        sample_size = int(self.population * self.trading_sample)
        trading_agents = random.sample(self.agents, k=sample_size)
        for agent_a, agent_b in itertools.combinations(trading_agents, 2):
            agent_a.trade(agent_b)
        self._snapshot(source=self.SOURCE_SESSION)

    def plot_histogram(self, **hist_kwargs) -> Figure:
        # Get the arguments
        hist_plot_kwargs = {
            **WEALTH_DISTR_DEFAULT_HIST_PLOT_KWARGS,
            **hist_kwargs
        }
        # Create the histogram
        (hist_plot, *_), *_ = self.get_data().hist(
            column="money",
            **hist_plot_kwargs
        )
        # Title
        hist_plot.set_title(f"Wealth Distribution (Epoch {self.current_epoch})", size=15)
        # Labels
        hist_plot.set_xlabel("Monetary Units ($$$)", labelpad=20, weight='bold', size=11)
        hist_plot.set_ylabel("Agents", labelpad=20, weight='bold', size=11)
        # Spines
        hist_plot.spines["top"].set_visible(False)
        hist_plot.spines["right"].set_visible(False)
        hist_plot.spines["left"].set_visible(False)
        # Y Ticks
        for tick in hist_plot.get_yticks():
            hist_plot.axhline(y=tick, linestyle='dashed', alpha=0.05, color=hist_plot_kwargs["color"], zorder=1)
        return hist_plot.get_figure()

    def plot_timeseries(self, use_sessions: bool = False, **line_kwargs) -> Figure:
        # Get the data
        data = pd.DataFrame(self.history).drop(["count", "std"], 1)
        filter_source = f"source == '{self.SOURCE_EPOCH}'"
        if use_sessions:
            filter_source = f"source == '{self.SOURCE_SESSION}'"
        data = data.query(filter_source).drop(["source"], 1)
        # Kwargs
        line_plot_kwargs = {
            **WEALTH_DISTR_DEFAULT_LINE_PLOT_KWARGS,
            **line_kwargs
        }
        # Create the plot
        line_plot = data.plot.line(**line_plot_kwargs)
        # Title
        line_plot.set_title("Wealth Gap Evolution", size=15)
        # Labels
        label = self.SOURCE_SESSION if use_sessions else self.SOURCE_EPOCH
        line_plot.set_xlabel(f"Time ({label.lower()})", labelpad=20, weight='bold', size=11)
        line_plot.set_ylabel("Money", labelpad=20, weight='bold', size=11)
        # Spines
        line_plot.spines["top"].set_visible(False)
        line_plot.spines["right"].set_visible(False)
        line_plot.spines["left"].set_visible(False)
        # Y Ticks
        for tick in line_plot.get_yticks():
            line_plot.axhline(y=tick, linestyle='dashed', alpha=0.05, color="black", zorder=1)
        return line_plot.get_figure()

    def plot_std(self, use_sessions: bool = False, **line_kwargs) -> Figure:
        # Get the data
        data = pd.DataFrame(self.history)[["source", "std"]]
        filter_source = f"source == '{self.SOURCE_EPOCH}'"
        if use_sessions:
            filter_source = f"source == '{self.SOURCE_SESSION}'"
        data = data.query(filter_source).drop(["source"], 1)
        # Kwargs
        line_plot_kwargs = {
            **WEALTH_DISTR_DEFAULT_LINE_PLOT_KWARGS,
            **line_kwargs
        }
        # Create the plot
        line_plot = data.plot.line(**line_plot_kwargs)
        # Title
        line_plot.set_title("STD Evolution", size=15)
        # Labels
        label = self.SOURCE_SESSION if use_sessions else self.SOURCE_EPOCH
        line_plot.set_xlabel(f"Time ({label.lower()})", labelpad=20, weight='bold', size=11)
        line_plot.set_ylabel("STD ($)", labelpad=20, weight='bold', size=11)
        # Spines
        line_plot.spines["top"].set_visible(False)
        line_plot.spines["right"].set_visible(False)
        line_plot.spines["left"].set_visible(False)
        # Y Ticks
        for tick in line_plot.get_yticks():
            line_plot.axhline(y=tick, linestyle='dashed', alpha=0.05, color="black", zorder=1)
        return line_plot.get_figure()
