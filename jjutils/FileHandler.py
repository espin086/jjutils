import pandas as pd
from pathlib import Path
import logging


class FileHandler:
    """Class to handle files."""

    def __init__(self, file_path):
        """Initializes the FileHandler with the provided file path.

        Args:
            file_path (str or Path): The path to the file to be handled.
        """
        self.file_path = Path(file_path)
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def read_csv(self, sep=","):
        """Reads a CSV file and returns a DataFrame.

        Args:
            sep (str): Delimiter to use. Default is ','.

        Returns:
            DataFrame or None: The content of the CSV file.
        """
        try:
            data = pd.read_csv(self.file_path, sep=sep)
            logging.info(f"Successfully read CSV file {self.file_path}")
            return data
        except FileNotFoundError:
            logging.error(f"File {self.file_path} not found")
            return None
        except Exception as e:
            logging.error(f"Error reading CSV file {self.file_path}: {e}")
            return None

    def read_file(self):
        """Reads a file and returns the content.

        Returns:
            str or None: The content of the file.
        """
        try:
            with self.file_path.open("r") as file:
                content = file.read()
            logging.info(f"Successfully read file {self.file_path}")
            return content
        except FileNotFoundError:
            logging.error(f"File {self.file_path} not found")
            return None
        except Exception as e:
            logging.error(f"Error reading file {self.file_path}: {e}")
            return None

    def write_file(self, content):
        """Writes content to a file.

        Args:
            content (str): Content to write to the file.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            with self.file_path.open("w") as file:
                file.write(content)
            logging.info(f"Successfully wrote to file {self.file_path}")
            return True
        except Exception as e:
            logging.error(f"Error writing to file {self.file_path}: {e}")
            return False

    def append_to_file(self, content):
        """Appends content to a file.

        Args:
            content (str): Content to append to the file.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            with self.file_path.open("a") as file:
                file.write(content)
            logging.info(f"Successfully appended to file {self.file_path}")
            return True
        except Exception as e:
            logging.error(f"Error appending to file {self.file_path}: {e}")
            return False

    def delete_file(self):
        """Deletes a file.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            self.file_path.unlink()
            logging.info(f"Successfully deleted file {self.file_path}")
            return True
        except FileNotFoundError:
            logging.error(f"File {self.file_path} not found")
            return False
        except Exception as e:
            logging.error(f"Error deleting file {self.file_path}: {e}")
            return False
