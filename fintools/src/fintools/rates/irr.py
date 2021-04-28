from typing import List, Union

import numpy as np


def irr(cashflows: List[float]) -> float:
    # Get polynomial roots
    # Note: we reverse the cashflows to have higher-order powers first.
    sol = np.roots(cashflows[::-1])
    # Select only the solutions that make sense
    # Criteria: no imaginary solution; real component greater than zero.
    candidates_filter = (sol.imag == 0) & (sol.real > 0)
    if not candidates_filter.any():
        return np.nan
    real_solutions = sol[candidates_filter].real
    # Transform back to "rate" from sol = 1 / (1 + rate)
    # Note: rates is still a list!
    rates = 1 / real_solutions - 1
    # Return only one result (nearest to zero)
    return rates[np.argmin(rates)]
