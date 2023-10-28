import pandas as pd
import numpy as np


class DataFrameCleaner:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def change_index(self, column):
        self.dataframe = self.dataframe.set_index(column)

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
        if new_type == "int":
            self.dataframe[column] = self.dataframe[column].fillna(0).astype(int)
        else:
            self.dataframe[column] = self.dataframe[column].astype(new_type)

    def remove_columns(self, columns):
        self.dataframe = self.dataframe.drop(columns, axis=1)

    def lower_case_column(self, column):
        self.dataframe[column] = self.dataframe[column].str.lower()

    def remove_white_spaces(self, column):
        self.dataframe[column] = self.dataframe[column].str.strip()

    def remove_special_characters(self, column):
        self.dataframe[column] = self.dataframe[column].str.replace("[^a-zA-Z0-9]", "")

    def clean_text_column(self, column):
        self.lower_case_column(column)
        self.remove_white_spaces(column)
        self.remove_special_characters(column)

    def get_cleaned_dataframe(self):
        return self.dataframe
