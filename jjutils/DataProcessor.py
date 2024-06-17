import pandas as pd
import numpy as np
import re
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DataFrameCleaner:
    """
    A class used to clean a pandas DataFrame.

    Attributes:
        dataframe : pd.DataFrame
            The dataframe to be cleaned.
    """

    def __init__(self, dataframe):
        """
        Initializes the DataFrameCleaner with a dataframe.

        Args:
            dataframe (pd.DataFrame): The dataframe to be cleaned.
        """
        self.dataframe = dataframe
        logging.info("DataFrame initialized for cleaning")

    def change_index(self, column):
        """Change the index of the DataFrame to the specified column."""
        self.dataframe = self.dataframe.set_index(column)
        logging.info(f"Index changed to {column}")

    def remove_duplicates(self):
        """Remove duplicate rows from DataFrame."""
        self.dataframe = self.dataframe.drop_duplicates()
        logging.info("Duplicates removed from DataFrame")

    def remove_missing_values(self):
        """Remove rows with missing values from DataFrame."""
        self.dataframe = self.dataframe.dropna()
        logging.info("Missing values removed from DataFrame")

    def remove_outliers(self, column, threshold):
        """Remove outliers from a specified column based on Z-score threshold."""
        z_scores = (
            self.dataframe[column] - self.dataframe[column].mean()
        ) / self.dataframe[column].std()
        self.dataframe = self.dataframe[
            (z_scores < threshold) & (z_scores > -threshold)
        ]
        logging.info(
            f"Outliers removed from column {column} with threshold {threshold}"
        )

    def convert_data_types(self, column, new_type):
        """Convert data type of a specified column."""
        if new_type == "int":
            self.dataframe[column] = self.dataframe[column].fillna(0).astype(int)
        else:
            self.dataframe[column] = self.dataframe[column].astype(new_type)
        logging.info(f"Column {column} converted to type {new_type}")

    def remove_columns(self, columns):
        """Remove specified columns from DataFrame."""
        self.dataframe = self.dataframe.drop(columns, axis=1)
        logging.info(f"Columns {columns} removed from DataFrame")

    def lower_case_column(self, column):
        """Convert all text in a specified column to lowercase."""
        self.dataframe[column] = self.dataframe[column].str.lower()
        logging.info(f"Text in column {column} converted to lowercase")

    def remove_white_spaces(self, column):
        """Remove leading and trailing white spaces in a specified column."""
        self.dataframe[column] = self.dataframe[column].str.strip()
        logging.info(f"Leading and trailing whitespaces removed from column {column}")

    def remove_special_characters(self, column):
        """Remove special characters in a specified column."""
        self.dataframe[column] = self.dataframe[column].str.replace(
            r"[^a-zA-Z0-9]", "", regex=True
        )
        logging.info(f"Special characters removed from column {column}")

    def clean_text_column(self, column):
        """Clean text in a specified column by converting to lowercase, removing white spaces and special characters."""
        self.lower_case_column(column)
        self.remove_white_spaces(column)
        self.remove_special_characters(column)
        logging.info(f"Text column {column} cleaned")

    def get_cleaned_dataframe(self):
        """Return the cleaned DataFrame."""
        logging.info("Returning cleaned DataFrame")
        return self.dataframe
