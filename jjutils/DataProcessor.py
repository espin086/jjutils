import pandas as pd


class DataFrameCleaner:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def remove_duplicates(self):
        self.dataframe = self.dataframe.drop_duplicates()

    def remove_missing_values(self):
        self.dataframe = self.dataframe.dropna()

    def remove_outliers(self, column, threshold):
        z_scores = (
            self.dataframe[column] - self.dataframe[column].mean()
        ) / self.dataframe[column].std()
        self.dataframe = self.dataframe[
            (z_scores < threshold) & (z_scores > -threshold)
        ]

    def convert_data_types(self, column, new_type):
        self.dataframe[column] = self.dataframe[column].astype(new_type)

    def remove_columns(self, columns):
        self.dataframe = self.dataframe.drop(columns, axis=1)

    def get_cleaned_dataframe(self):
        return self.dataframe
