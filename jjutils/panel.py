import pandas as pd
import numpy as np
import logging

import statsmodels.api as sm
from linearmodels.panel import PanelOLS, RandomEffects
from scipy.stats import chi2


class BaseRegression:
    def __init__(self, data, dependent_var, independent_vars, panel_var):
        self.data = data
        self.dependent_var = dependent_var
        self.independent_vars = independent_vars
        self.panel_var = panel_var
        self.results = None
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler())

    def fit(self):
        raise NotImplementedError

    def print_report(self):
        if self.results is None:
            raise ValueError("Model not fitted yet.")
        print("Regression Results:")
        print(self.results)


class OLSRegression(BaseRegression):
    def fit(self):
        X = sm.add_constant(self.data[self.independent_vars])
        y = self.data[self.dependent_var]
        model = sm.OLS(y, X)
        self.results = model.fit()

    def print_report(self):
        if self.results is None:
            raise ValueError("Model not fitted yet.")
        print("Regression Results:")
        print(self.results.summary())


class FixedEffectsRegression(BaseRegression):
    def fit(self):
        panel_data = self.data.set_index([self.panel_var, self.data.index])
        model = PanelOLS.from_formula(
            f"{self.dependent_var} ~ 1 + {' + '.join(self.independent_vars)}",
            data=panel_data,
        )
        self.results = model.fit(cov_type="robust")

    def print_report(self):
        super().print_report()
        print("\nFixed Effects Model Summary:")
        print(self.results.summary)


class RandomEffectsRegression(BaseRegression):
    def fit(self):
        panel_data = self.data.set_index([self.panel_var, self.data.index])
        model = RandomEffects.from_formula(
            f"{self.dependent_var} ~ 1 + {' + '.join(self.independent_vars)}",
            data=panel_data,
        )
        self.results = model.fit()

    def print_report(self):
        super().print_report()
        print("\nRandom Effects Model Summary:")
        print(self.results.summary)


def main():
    # Example usage
    data = pd.DataFrame(
        {
            "Panel": ["A", "A", "B", "B", "C", "C"],
            "Dependent": [1, 2, 3, 4, 5, 6],
            "Independent": [7, 8, 9, 10, 11, 12],
        }
    )
    model = RandomEffectsRegression(data, "Dependent", ["Independent"], "Panel")
    model.fit()
    model.print_report()


if __name__ == "__main__":
    main()
