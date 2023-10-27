import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class DataExplorer:
    def __init__(self, df):
        self.df = df

    def plot_histogram(self, column, bins=10):
        sns.histplot(self.df[column], bins=bins, kde=True)
        plt.title(f'Histogram for {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    def plot_boxplot(self, x, y):
        sns.boxplot(x=x, y=y, data=self.df)
        plt.title(f'Box Plot: {x} vs {y}')
        plt.show()

    def plot_pairplot(self, hue=None):
        sns.pairplot(self.df, hue=hue)
        plt.title('Pair Plot')
        plt.show()

    def plot_heatmap(self):
        correlation_matrix = self.df.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.show()

    def plot_countplot(self, column, hue=None):
        sns.countplot(x=column, hue=hue, data=self.df)
        plt.title(f'Count Plot for {column}')
        plt.show()

    def plot_barplot(self, x, y, hue=None):
        sns.barplot(x=x, y=y, hue=hue, data=self.df)
        plt.title(f'Bar Plot: {x} vs {y}')
        plt.show()

    def explore_data(self):
        print("Dataset Summary:")
        print(self.df.info())
        print("\nDescriptive Statistics:")
        print(self.df.describe())

    def display_head(self, n=5):
        return self.df.head(n)

    def display_tail(self, n=5):
        return self.df.tail(n)