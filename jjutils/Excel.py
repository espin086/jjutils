import pandas as pd


class ExcelHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.dataframes = {}

    def read_sheet(self, sheet_name):
        """
        Read a specific sheet from the Excel file.

        :param sheet_name: Name of the sheet to read.
        :return: DataFrame containing the sheet data.
        """
        try:
            df = pd.read_excel(self.file_path, sheet_name=sheet_name)
            self.dataframes[sheet_name] = df
            return df
        except Exception as e:
            print(f"Error reading sheet {sheet_name}: {e}")

    def read_all_sheets(self):
        """
        Read all sheets from the Excel file.

        :return: Dictionary with sheet names as keys and DataFrames as values.
        """
        try:
            xls = pd.ExcelFile(self.file_path)
            for sheet_name in xls.sheet_names:
                self.dataframes[sheet_name] = pd.read_excel(xls, sheet_name=sheet_name)
            return self.dataframes
        except Exception as e:
            print(f"Error reading all sheets: {e}")

    def save_sheet(self, df, sheet_name):
        """
        Save a DataFrame to a specific sheet in the Excel file.

        :param df: DataFrame to save.
        :param sheet_name: Name of the sheet to save the DataFrame to.
        """
        try:
            with pd.ExcelWriter(
                self.file_path, engine="openpyxl", mode="a", if_sheet_exists="replace"
            ) as writer:
                df.to_excel(writer, sheet_name=sheet_name, index=False)
            self.dataframes[sheet_name] = df
        except Exception as e:
            print(f"Error saving sheet {sheet_name}: {e}")

    def save_all_sheets(self):
        """
        Save all DataFrames in the dataframes dictionary to the Excel file.
        """
        try:
            with pd.ExcelWriter(self.file_path, engine="openpyxl") as writer:
                for sheet_name, df in self.dataframes.items():
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
        except Exception as e:
            print(f"Error saving all sheets: {e}")

    def get_dataframe(self, sheet_name):
        """
        Get the DataFrame of a specific sheet.

        :param sheet_name: Name of the sheet.
        :return: DataFrame containing the sheet data.
        """
        return self.dataframes.get(sheet_name, None)

    def list_sheets(self):
        """
        List all sheet names in the Excel file.

        :return: List of sheet names.
        """
        try:
            xls = pd.ExcelFile(self.file_path)
            return xls.sheet_names
        except Exception as e:
            print(f"Error listing sheets: {e}")
            return []
