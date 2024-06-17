import pandas as pd
import logging
import statsmodels.api as sm
from linearmodels.panel import PanelOLS, RandomEffects
from base_regression import BaseRegression


class OLSRegression(BaseRegression):
    """
    OLS Regression implementation inheriting from BaseRegression.
    """

    def fit(self):
        """
        Fit the OLS model to the data.

        Raises:
            ValueError: If the data is not set correctly.
        """
        X = sm.add_constant(self.data[self.independent_vars])
        y = self.data[self.dependent_var]
        model = sm.OLS(y, X)
        self.results = model.fit()

    def print_report(self):
        """
        Print the regression results.

        Raises:
            ValueError: If the model is not yet fitted.
        """
        if self.results is None:
            raise ValueError("Model not fitted yet.")
        print("Regression Results:")
        print(self.results.summary())


class FixedEffectsRegression(BaseRegression):
    """
    Fixed Effects Regression implementation inheriting from BaseRegression.
    """

    def fit(self):
        """
        Fit the Fixed Effects model to the data.

        Raises:
            ValueError: If the data is not set correctly.
        """
        panel_data = self.data.set_index([self.panel_var, self.data.index])
        model = PanelOLS.from_formula(
            f"{self.dependent_var} ~ 1 + {' + '.join(self.independent_vars)}",
            data=panel_data,
        )
        self.results = model.fit(cov_type="robust")

    def print_report(self):
        """
        Print the regression results.

        Raises:
            ValueError: If the model is not yet fitted.
        """
        super().print_report()
        print("\nFixed Effects Model Summary:")
        print(self.results.summary())


class RandomEffectsRegression(BaseRegression):
    """
    Random Effects Regression implementation inheriting from BaseRegression.
    """

    def fit(self):
        """
        Fit the Random Effects model to the data.

        Raises:
            ValueError: If the data is not set correctly.
        """
        panel_data = self.data.set_index([self.panel_var, self.data.index])
        model = RandomEffects.from_formula(
            f"{self.dependent_var} ~ 1 + {' + '.join(self.independent_vars)}",
            data=panel_data,
        )
        self.results = model.fit()

    def print_report(self):
        """
        Print the regression results.

        Raises:
            ValueError: If the model is not yet fitted.
        """
        super().print_report()
        print("\nRandom Effects Model Summary:")
        print(self.results.summary())
