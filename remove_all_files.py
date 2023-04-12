#!/usr/bin/env python3


"""Delete all files in the specified folder.

example usage: 
    /usr/bin/python3 /Users/jjespinoza/Documents/repos/Utilities/remove_all_files.py /Users/jjespinoza/Desktop
    /usr/bin/python3 /Users/jjespinoza/Documents/repos/Utilities/remove_all_files.py /Users/jjespinoza/Downloads

Note: This script will not delete any subfolders or files in subfolders.

"""

import os
import argparse
import logging


def delete_files_in_folder(folder_path):
    """Delete all files in the specified folder."""
    if not os.path.exists(folder_path):
        logging.error(f"The folder {folder_path} does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                logging.info(f"Deleted: {file_path}")
            else:
                logging.info(f"{file_path} is not a file.")
        except Exception as e:
            logging.error(f"Error deleting {file_path}: {e}")


def main():
    """Delete all files in the specified folder."""
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Set up command line argument parsing
    parser = argparse.ArgumentParser(
        description="Delete all files in the specified folder."
    )
    parser.add_argument(
        "folder_path", help="The path to the folder whose files you want to delete."
    )
    args = parser.parse_args()

    # Delete files in the specified folder
    delete_files_in_folder(args.folder_path)


if __name__ == "__main__":
    main()
