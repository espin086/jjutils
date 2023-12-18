from jjutils import config
from jjutils.FileHandler import FileHandler
from jjutils.DataExplorer import DataFrameExplorer
from jjutils.DataProcessor import DataFrameCleaner


def update_data_types(df):
    """Updates the data types of the dataframe."""
    # checking and cleaning the dataframe
    explorer = DataFrameExplorer(df)
    data_cleaner = DataFrameCleaner(df)
    # change PassengerID to string
    data_cleaner.convert_data_types("PassengerId", "str")
    # changed the Survived column to boolean
    data_cleaner.convert_data_types("Survived", "bool")
    # changing the Pclass column to category
    data_cleaner.convert_data_types("Pclass", "category")
    # convert Sex into a category
    data_cleaner.convert_data_types("Sex", "category")
    # changing the Age columng to int
    data_cleaner.convert_data_types("Age", "int")
    # changing cabin column to category
    data_cleaner.convert_data_types("Cabin", "category")
    # checking the Embarked column and correcting dtype
    data_cleaner.convert_data_types("Embarked", "category")
    # changing the index to PassengerId
    data_cleaner.change_index("PassengerId")
    # final dataframe with correct datatypes
    # showing final data types
    dtypes = explorer.check_datatypes()
    print(dtypes)
    return data_cleaner.get_cleaned_dataframe()


# importing CSV file into a dataframe
def main():
    file_handler = FileHandler(config.CSV_PATH)
    df = file_handler.read_csv()
    df = update_data_types(df)
    data_cleaner = DataFrameCleaner(df)
    data_cleaner.remove_duplicates()
    data_cleaner.clean_text_column("Name")
    return data_cleaner.get_cleaned_dataframe()


if __name__ == "__main__":
    main()
