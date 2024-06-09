import pandas as pd
import os


class CSVHandler:
    def __init__(self, file_path, delimiter=","):
        self.file_path = file_path
        self.delimiter = delimiter
        self.dataframe = None

        # Check if file exists, if not create it
        if not os.path.isfile(self.file_path):
            open(self.file_path, "w").close()

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


def main():
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
