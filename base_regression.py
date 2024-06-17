import logging


class BaseRegression:
    """
    A base class for regression with common functionalities.
    """

    def __init__(self, data, dependent_var, independent_vars, panel_var):
        """
        Initialize the BaseRegression class.

        Args:
            data (pd.DataFrame): The dataset.
            dependent_var (str): The dependent variable name.
            independent_vars (list): List of independent variable names.
            panel_var (str): The panel variable name.
        """
        self.data = data
        self.dependent_var = dependent_var
        self.independent_vars = independent_vars
        self.panel_var = panel_var
        self.results = None
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler())

    def fit(self):
        """
        A placeholder method to fit the model, to be implemented by subclasses.
        """
        raise NotImplementedError

    def print_report(self):
        """
        Print the regression results.

        Raises:
            ValueError: If the model is not fitted yet.
        """
        if self.results is None:
            raise ValueError("Model not fitted yet.")
        print("Regression Results:")
        print(self.results)
