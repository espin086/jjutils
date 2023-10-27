import pandas as pd

class DataFrameCleaner:
    def __init__(self, df):
        self.df = df

    def remove_duplicates(self, subset=None):
        self.df = self.df.drop_duplicates(subset=subset)
        return self

    def remove_missing_values(self, axis=0, how='any', subset=None):
        self.df = self.df.dropna(axis=axis, how=how, subset=subset)
        return self

    def fill_missing_values(self, value, subset=None):
        self.df = self.df.fillna(value, subset=subset)
        return self

    def convert_data_types(self, column_types):
        self.df = self.df.astype(column_types)
        return self

    def rename_columns(self, column_mapping):
        self.df = self.df.rename(columns=column_mapping)
        return self

    def drop_columns(self, columns):
        self.df = self.df.drop(columns, axis=1)
        return self

    def reset_index(self, drop=False):
        self.df = self.df.reset_index(drop=drop)
        return self

    def get_cleaned_dataframe(self):
        return self.df

    def describe_data(self):
        return self.df.describe()

    def display_head(self, n=5):
        return self.df.head(n)

    def display_tail(self, n=5):
        return self.df.tail(n)