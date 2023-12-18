import pandas


class FileHandler:
    """Class to handle files."""

    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self, sep=","):
        """Reads a CSV file and returns a dataframe."""
        try:
            return pandas.read_csv(self.file_path, sep=sep)
        except FileNotFoundError:
            return None

    def read_file(self):
        """Reads a file and returns the content."""
        try:
            with open(self.file_path, "r") as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return None

    def write_file(self, content):
        """Writes content to a file."""
        try:
            with open(self.file_path, "w") as file:
                file.write(content)
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False

    def append_to_file(self, content):
        """Appends content to a file."""
        try:
            with open(self.file_path, "a") as file:
                file.write(content)
            return True
        except Exception as e:
            print(f"Error appending to file: {e}")
            return False

    def delete_file(self):
        try:
            import os

            os.remove(self.file_path)
            return True
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"Error deleting file: {e}")
            return False
