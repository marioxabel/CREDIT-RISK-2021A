from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd

from fintools.rates import Cetes28, Cetes91, Cetes182
from fintools.rates.cetes import Cetes


class Main:

    @staticmethod
    def hello(name: Optional[str] = None):
        if name is None:
            name = "world"
        return f"Hello, {name}!"

    @staticmethod
    def table(
            cetes28: bool = False,
            cetes91: bool = False,
            cetes182: bool = False,
            start: Optional[str] = None,
            end: Optional[str] = None,
            save_file: Optional[str] = None,
            show: bool = False
    ):
        data = pd.DataFrame([], columns=["date"])
        if cetes28:
            df_28 = Cetes28(date_start=start, date_end=end)\
                .get_dataframe().rename(columns={"value": "cetes28"})
            data = data.merge(df_28, left_on='date', right_on='date', how="outer")
        if cetes91:
            df_91 = Cetes91(date_start=start, date_end=end)\
                .get_dataframe().rename(columns={"value": "cetes91"})
            data = data.merge(df_91, left_on='date', right_on='date', how="outer")
        if cetes182:
            df_182 = Cetes182(date_start=start, date_end=end) \
                .get_dataframe().rename(columns={"value": "cetes182"})
            data = data.merge(df_182, left_on='date', right_on='date', how="outer")
        if save_file is not None:
            data.to_csv(save_file, index=False)
        if show:
            return data.reset_index(drop=True).to_string()

    @staticmethod
    def plot(
            tag: str,
            start: Optional[str] = None,
            end: Optional[str] = None,
            save_file: Optional[str] = None,
            show: bool = False
    ):
        # Create the cetes instance
        cetes = Cetes(tag=str(tag), date_start=start, date_end=end)
        # Create the plot
        plot = cetes.get_dataframe().plot(x="date", y="value")
        plt.title(f"CETES {tag}")
        plt.ylabel("Rate")
        plt.grid()
        # Get the figure from the plot
        figure = plot.get_figure()
        # Show figure if requested
        if show:
            plt.show()
        # Save file if requested
        if save_file is not None:
            figure.savefig(save_file)
