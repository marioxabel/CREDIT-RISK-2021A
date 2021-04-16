import fire
import pandas as pd

from .main import Main


if __name__ == "__main__":
    pd.options.display.float_format = '${:,.2f}'.format
    fire.Fire(Main)
