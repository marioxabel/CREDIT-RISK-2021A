import os


# Base path
WEALTH_DISTR_BASE_PATH = os.environ.get(
    "WEALTH_DISTR_BASE_PATH",
    default=os.path.dirname(os.path.abspath(__file__))
)
# Simulations
WEALTH_DISTR_SIMULATIONS_DIRECTORY = os.environ.get(
    "WEALTH_DISTR_SIMULATIONS_DIRECTORY",
    default="simulations"
)
WEALTH_DISTR_SIMULATIONS_PATH = os.path.join(WEALTH_DISTR_BASE_PATH, WEALTH_DISTR_SIMULATIONS_DIRECTORY)

# Figures
WEALTH_DISTR_PLOTS_DIRECTORY = os.environ.get(
    "WEALTH_DISTR_PLOTS_DIRECTORY",
    default="plots"
)
WEALTH_DISTR_PLOTS_PATH = os.path.join(WEALTH_DISTR_BASE_PATH, WEALTH_DISTR_PLOTS_DIRECTORY)

# Plot configs
WEALTH_DISTR_DEFAULT_HIST_PLOT_KWARGS = {
    "color": "#1f77b4",
    "grid": False,
    "zorder": 2,
    "rwidth": 0.9,
    "alpha": 0.8,
    "figsize": (10, 4)
}

WEALTH_DISTR_DEFAULT_LINE_PLOT_KWARGS = {
    "style": "-",
    "legend": True,
    "figsize": (10, 4)
}
