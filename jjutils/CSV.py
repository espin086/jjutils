import pandas as pd


class CSVHandler:
    def __init__(self, file_path, delimiter="|"):
        self.file_path = file_path
        self.delimiter = delimiter
        self.dataframe = None

    def read_csv(self):
        """
        Read the CSV file with the specified delimiter.

        :return: DataFrame containing the CSV data.
        """
        try:
            self.dataframe = pd.read_csv(self.file_path, delimiter=self.delimiter)
            return self.dataframe
        except Exception as e:
            print(f"Error reading CSV file: {e}")

    def save_csv(self, df, index=False):
        """
        Save a DataFrame to the CSV file with the specified delimiter.

        :param df: DataFrame to save.
        :param index: Boolean flag to include index in CSV. Default is False.
        """
        try:
            df.to_csv(self.file_path, delimiter=self.delimiter, index=index)
            self.dataframe = df
        except Exception as e:
            print(f"Error saving CSV file: {e}")

    def append_csv(self, df, index=False):
        """
        Append a DataFrame to the existing CSV file with the specified delimiter.

        :param df: DataFrame to append.
        :param index: Boolean flag to include index in CSV. Default is False.
        """
        try:
            df.to_csv(
                self.file_path,
                mode="a",
                header=False,
                delimiter=self.delimiter,
                index=index,
            )
            if self.dataframe is not None:
                self.dataframe = pd.concat([self.dataframe, df], ignore_index=True)
            else:
                self.dataframe = df
        except Exception as e:
            print(f"Error appending to CSV file: {e}")

    def update_csv(self, df, index=False):
        """
        Update the CSV file with a new DataFrame, overwriting existing content.

        :param df: DataFrame to save.
        :param index: Boolean flag to include index in CSV. Default is False.
        """
        self.save_csv(df, index=index)
        self.dataframe = df

    def get_dataframe(self):
        """
        Get the DataFrame of the CSV data.

        :return: DataFrame containing the CSV data.
        """
        return self.dataframe
