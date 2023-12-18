import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class DataFrameExplorer:
    """Class to explore a dataframe."""

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def check_head(self, n=5):
        """Returns the first n rows of the dataframe."""
        return self.dataframe.head(n)

    def check_datatypes(self):
        """Returns the data types of the dataframe."""
        return self.dataframe.dtypes

    def check_missing_variables(self):
        """Returns the number of missing variables in the dataframe."""
        return self.dataframe.isnull().sum()

    def make_correlation_plot(self):
        """Makes a correlation plot of the dataframe."""
        corr_matrix = self.dataframe.corr()
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
        plt.title("Correlation Plot")
        plt.show()

    def make_histograms(self):
        """Makes histograms of the dataframe."""
        self.dataframe.hist(figsize=(10, 10))
        plt.tight_layout()
        plt.show()

    def make_box_plots(self):
        """Makes box plots of the dataframe."""
        self.dataframe.plot(kind="box", figsize=(10, 6))
        plt.title("Box Plot")
        plt.show()

    def run(self):
        """Runs all methods."""
        print(self.check_head())
        print(self.check_datatypes())
        print(self.check_missing_variables())
        self.make_correlation_plot()
        self.make_histograms()
        self.make_box_plots()
