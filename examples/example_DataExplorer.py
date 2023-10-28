from jjutils import config
from jjutils.FileHandler import FileHandler

file_handler = FileHandler(config.CSV_PATH)
csv = file_handler.read_csv()
print(csv)
