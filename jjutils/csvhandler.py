import pandas as pd
import logging
import os


class CSVHandler:
    """Class to handle CSV files."""

    def __init__(self, file_path, delimiter=","):
        """
        Initialize the CSVHandler.

        Args:
            file_path (str): Path to the CSV file.
            delimiter (str): Delimiter used in the CSV file.
        """
        self.file_path = file_path
        self.delimiter = delimiter
        self.dataframe = None
        self.logger = logging.getLogger(__name__)

        # Check if file exists, if not create it
        if not os.path.isfile(self.file_path):
            open(self.file_path, "w").close()

    def read_csv(self):
        """
        Read the CSV file with the specified delimiter.

        Returns:
            DataFrame: DataFrame containing the CSV data.
        """
        try:
            self.dataframe = pd.read_csv(self.file_path, delimiter=self.delimiter)
            self.logger.info(f"Successfully read CSV file: {self.file_path}")
            return self.dataframe
        except Exception as e:
            self.logger.error(f"Error reading CSV file: {e}")
            return None

    def save_csv(self, df, index=False):
        """
        Save a DataFrame to the CSV file with the specified delimiter.

        Args:
            df (DataFrame): DataFrame to save.
            index (bool): Boolean flag to include index in CSV. Default is False.
        """
        try:
            df.to_csv(self.file_path, delimiter=self.delimiter, index=index)
            self.dataframe = df
            self.logger.info(
                f"Successfully saved DataFrame to CSV file: {self.file_path}"
            )
        except Exception as e:
            self.logger.error(f"Error saving CSV file: {e}")

    def append_csv(self, df, index=False):
        """
        Append a DataFrame to the existing CSV file with the specified delimiter.

        Args:
            df (DataFrame): DataFrame to append.
            index (bool): Boolean flag to include index in CSV. Default is False.
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
            self.logger.info(
                f"Successfully appended data to CSV file: {self.file_path}"
            )
        except Exception as e:
            self.logger.error(f"Error appending to CSV file: {e}")

    def update_csv(self, df, index=False):
        """
        Update the CSV file with a new DataFrame, overwriting existing content.

        Args:
            df (DataFrame): DataFrame to save.
            index (bool): Boolean flag to include index in CSV. Default is False.
        """
        self.save_csv(df, index=index)
        self.dataframe = df

    def get_dataframe(self):
        """
        Get the DataFrame of the CSV data.

        Returns:
            DataFrame: DataFrame containing the CSV data.
        """
        return self.dataframe


def main():
    # Initialize logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Create a DataFrame
    data = {
        "Name": ["John", "Anna", "Peter", "Linda"],
        "Age": [28, 24, 35, 32],
        "City": ["New York", "Paris", "Berlin", "London"],
    }
    df = pd.DataFrame(data)

    # Create a CSVHandler for a new CSV file
    csv_handler = CSVHandler("data/train.csv")

    # Save the DataFrame to the CSV file
    csv_handler.save_csv(df)

    # Read the CSV file
    df_read = csv_handler.read_csv()
    print(df_read)

    # Append data to the CSV file
    append_data = {
        "Name": ["Tom", "Jerry"],
        "Age": [30, 25],
        "City": ["Tokyo", "Delhi"],
    }
    df_append = pd.DataFrame(append_data)
    csv_handler.append_csv(df_append)

    # Read the updated CSV file
    df_updated = csv_handler.read_csv()
    print(df_updated)

    # Update the CSV file with new data
    update_data = {
        "Name": ["Alice", "Bob"],
        "Age": [27, 33],
        "City": ["Sydney", "Toronto"],
    }
    df_update = pd.DataFrame(update_data)
    csv_handler.update_csv(df_update)

    # Read the updated CSV file
    df_updated = csv_handler.read_csv()
    print(df_updated)


if __name__ == "__main__":
    main()
