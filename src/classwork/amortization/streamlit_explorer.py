import os

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from settings import (
    AMORTIZATION_CONFIG_DIRPATH,
    AMORTIZATION_TABLE_DIRPATH
)


@st.cache
def get_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def format_option(filename: str):
    config_file = filename.replace(".csv", ".json")
    config_path = os.path.join(AMORTIZATION_CONFIG_DIRPATH, config_file)
    with open(config_path, "r") as file:
        content = file.read()
    return content


def get_figure(df: pd.DataFrame) -> plt.Figure:
    annuity = df.annuity[1:].unique().tolist().pop()
    plot = df.plot.bar(x="t", y=["principal", "interest"], stacked=True)
    plt.title("Amortization Payments: ${:,.2f}".format(annuity))
    plt.ylabel("$$$")
    plt.grid()
    return plot.get_figure()


def app():
    st.markdown("# Amortization Explorer")

    options = [
        file
        for file in os.listdir(AMORTIZATION_TABLE_DIRPATH)
        if file.endswith(".csv")
    ]

    file = st.selectbox(
        label="Choose the config:",
        options=options,
        format_func=format_option
    )

    st.markdown("## Amortization Table")
    table = get_data(path=os.path.join(AMORTIZATION_TABLE_DIRPATH, file))
    st.write(table)

    st.markdown("## Payment contribution")
    figure = get_figure(df=table)
    st.pyplot(figure)


app()
