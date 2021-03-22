from typing import Optional
import datetime as dt

import pandas as pd
import requests

cetes_tags = {
    "28": "SF43936,CF107,5",
    "91": "SF43939,CF107,9",
    "182": "SF43942,CF107,13"
}


def get_data(s: str) -> pd.DataFrame:
    url = f"https://www.banxico.org.mx/SieInternet/consultaSerieGrafica.do?s={s}&versionSerie=LA-MAS-RECIENTE&l=es"
    return pd.DataFrame(requests.get(url).json()["valores"], columns=["date", "value"]) \
        .query("value > -100")


class Cetes:

    def __init__(self, tag: str, date_start: Optional[str] = None, date_end: Optional[str] = None):
        self.series = cetes_tags[tag]
        self.date_start = date_start
        self.date_end = date_end
        self.latest_dataframe = None
        self.latest_request_timestamp = None

    def _date_filter(self, data: pd.DataFrame) -> str:
        date_start = data.date.values[0] if self.date_start is None else self.date_start
        date_end = data.date.values[-1] if self.date_end is None else self.date_end
        return "'{start}' <= date <= '{end}'".format(
            start=date_start,
            end=date_end
        )

    def get_dataframe(self, cache: bool = False):
        if cache and self.latest_dataframe is not None:
            return self.latest_dataframe
        # Get all history
        data = get_data(s=self.series)
        # Get date filter
        date_filter = self._date_filter(data)
        # Update metadata
        self.latest_dataframe = data.assign(date=pd.to_datetime(data.date, infer_datetime_format=True)).query(
            date_filter)
        self.latest_request_timestamp = dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        return self.latest_dataframe


class Cetes28(Cetes):
    TAG = "28"

    def __init__(self, date_start: Optional[str] = None, date_end: Optional[str] = None):
        super().__init__(tag=self.TAG, date_start=date_start, date_end=date_end)


class Cetes91(Cetes):
    TAG = "91"

    def __init__(self, date_start: Optional[str] = None, date_end: Optional[str] = None):
        super().__init__(tag=self.TAG, date_start=date_start, date_end=date_end)


class Cetes182(Cetes):
    TAG = "182"

    def __init__(self, date_start: Optional[str] = None, date_end: Optional[str] = None):
        super().__init__(tag=self.TAG, date_start=date_start, date_end=date_end)
