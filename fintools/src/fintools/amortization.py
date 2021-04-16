from typing import Dict

import pandas as pd


class Amortization:

    def __init__(self, amount: float, rate: float, n: int):
        self.amount = amount
        self.rate = rate
        self.n = n

    def to_dict(self) -> Dict:
        return {
            "amount": self.amount,
            "rate": self.rate,
            "n": self.n
        }

    @property
    def annuity(self):
        return self.rate * self.amount / (1 - (1 + self.rate) ** (-self.n))

    def get_table(self) -> pd.DataFrame:
        b = self.amount
        a = self.annuity
        rows = [{"t": 0, "balance": b}]
        for t in range(1, self.n + 1):
            i = self.rate * b
            p = a - i
            b = b - p
            rows.append({
                "t": t,
                "principal": p,
                "interest": i,
                "annuity": a,
                "balance": b
            })
        return pd.DataFrame(rows)
