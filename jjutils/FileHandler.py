class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return None

    def write_file(self, content):
        try:
            with open(self.file_path, 'w') as file:
                file.write(content)
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False

    def append_to_file(self, content):
        try:
            with open(self.file_path, 'a') as file:
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
