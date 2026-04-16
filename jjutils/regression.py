import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan
import matplotlib.pyplot as plt


class RegressionAnalysis:
    def __init__(self, dataframe, formula):
        """
        Initialize the RegressionAnalysis with a Pandas DataFrame and a formula.

        :param dataframe: Pandas DataFrame containing the data.
        :param formula: Formula for the regression model (e.g., 'y ~ x1 + x2').
        """
        self.dataframe = dataframe
        self.formula = formula
        self.model = None
        self.results = None

    def fit_model(self):
        """
        Fit the regression model using the provided formula and data.

        :return: Fitted regression model results.
        """
        try:
            self.model = smf.ols(formula=self.formula, data=self.dataframe)
            self.results = self.model.fit()
            return self.results
        except Exception as e:
            print(f"Error fitting model: {e}")
            return None

    def summary(self):
        """
        Print the summary of the fitted regression model.
        """
        if self.results:
            print(self.results.summary())
        else:
            print("Model has not been fitted yet.")

    def plot_diagnostics(self):
        """
        Plot regression diagnostics.
        """
        if self.results:
            for predictor in [name for name in self.model.exog_names if name != "Intercept"]:
                sm.graphics.plot_regress_exog(self.results, predictor)
                plt.show()
        else:
            print("Model has not been fitted yet.")

    def calculate_vif(self):
        """
        Calculate Variance Inflation Factor (VIF) for the independent variables.

        :return: DataFrame containing VIF values.
        """
        if self.results:
            X = self.model.exog
            vif_data = pd.DataFrame()
            vif_data["variable"] = self.model.exog_names
            vif_data["VIF"] = [variance_inflation_factor(X, i) for i in range(X.shape[1])]
            return vif_data
        else:
            print("Model has not been fitted yet.")
            return None

    def residuals_histogram(self):
        """
        Plot a histogram of the residuals.
        """
        if self.results:
            residuals = self.results.resid
            plt.hist(residuals, bins=30, edgecolor="k")
            plt.title("Residuals Histogram")
            plt.xlabel("Residuals")
            plt.ylabel("Frequency")
            plt.show()
        else:
            print("Model has not been fitted yet.")

    def check_heteroscedasticity(self):
        """
        Perform Breusch-Pagan test for heteroscedasticity.

        :return: Test statistic and p-value.
        """
        if self.results:
            _, pval, __, f_pval = het_breuschpagan(self.results.resid, self.results.model.exog)
            return {"Lagrange multiplier p-value": pval, "F-statistic p-value": f_pval}
        else:
            print("Model has not been fitted yet.")
            return None

    def check_autocorrelation(self):
        """
        Perform Durbin-Watson test for autocorrelation.

        :return: Durbin-Watson statistic.
        """
        if self.results:
            dw = sm.stats.durbin_watson(self.results.resid)
            return dw
        else:
            print("Model has not been fitted yet.")
            return None

    def qq_plot(self):
        """
        Generate a QQ plot of the residuals to check for normality.
        """
        if self.results:
            sm.qqplot(self.results.resid, line="s")
            plt.title("QQ Plot")
            plt.show()
        else:
            print("Model has not been fitted yet.")

    def leverage_plot(self):
        """
        Generate a leverage plot to detect influential points.
        """
        if self.results:
            sm.graphics.influence_plot(self.results, criterion="cooks")
            plt.show()
        else:
            print("Model has not been fitted yet.")

    def set_dataframe(self, dataframe):
        """
        Set a new DataFrame for regression analysis.

        :param dataframe: Pandas DataFrame to use for regression analysis.
        """
        self.dataframe = dataframe

    def set_formula(self, formula):
        """
        Set a new formula for regression analysis.

        :param formula: Formula for the regression model (e.g., 'y ~ x1 + x2').
        """
        self.formula = formula

    def run_all_diagnostics(self):
        """
        Run all regression diagnostics and print the results.
        """
        if not self.results:
            print("Model has not been fitted yet.")
            return

        self.summary()

        vif_data = self.calculate_vif()
        print("\nVariance Inflation Factor (VIF):")
        print(vif_data)

        print("\nResiduals Histogram:")
        self.residuals_histogram()

        heteroscedasticity_test = self.check_heteroscedasticity()
        print("\nHeteroscedasticity Test (Breusch-Pagan):")
        print(heteroscedasticity_test)

        autocorrelation_test = self.check_autocorrelation()
        print("\nAutocorrelation Test (Durbin-Watson):")
        print(f"Durbin-Watson statistic: {autocorrelation_test}")

        print("\nQQ Plot:")
        self.qq_plot()

        print("\nLeverage Plot:")
        self.leverage_plot()

    def predict(self, new_data):
        """
        Predict the response for a new dataset.

        :param new_data: Pandas DataFrame containing the new data.
        :return: Predictions as a Pandas Series.
        """
        if self.results:
            try:
                predictions = self.results.predict(new_data)
                return predictions
            except Exception as e:
                print(f"Error making predictions: {e}")
                return None
        else:
            print("Model has not been fitted yet.")
            return None
