from jjutils import config
from jjutils.FileHandler import FileHandler
from jjutils.DataExplorer import DataFrameExplorer

file_handler = FileHandler(config.CSV_PATH)
df = file_handler.read_csv()

df_explorer = DataFrameExplorer(df)

df_explorer.run()
