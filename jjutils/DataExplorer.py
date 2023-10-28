import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class DataFrameExplorer:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def check_head(self, n=5):
        return self.dataframe.head(n)

    def check_datatypes(self):
        return self.dataframe.dtypes

    def check_missing_variables(self):
        return self.dataframe.isnull().sum()

    def make_correlation_plot(self):
        corr_matrix = self.dataframe.corr()
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
        plt.title("Correlation Plot")
        plt.show()

    def make_histograms(self):
        self.dataframe.hist(figsize=(10, 10))
        plt.tight_layout()
        plt.show()

    def make_box_plots(self):
        self.dataframe.plot(kind="box", figsize=(10, 6))
        plt.title("Box Plot")
        plt.show()
