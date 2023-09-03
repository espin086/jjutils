"""
Example of how to use the class: 

import JSONFileCRUD
file = JSONFileCRUD.JSONFileCRUD("url.json")

#create
data = {"test": 3}
file.create(data)
data = {"url": 5}
file.create(data)

#update
file.update(0, {'test': 4})

#view
file.read()

#delete
file.delete(0) 

"""


import argparse
import json


class JSONFileCRUD:
    """A class to handle basic CRUD operations on a JSON file.

    Attributes:
    file_name (str): the name of the file
    """

    def __init__(self, file_name):
        """Initialize the JSONFileCRUD class

        Arguments:
        file_name (str): the name of the file
        """
        self.file_name = file_name
        with open(self.file_name, "w") as file:
            json.dump([], file)

    def create(self, data):
        try:
            with open(self.file_name, "x") as file:
                pass
        except FileExistsError:
            pass
        with open(self.file_name, "r") as file:
            data_list = json.load(file)
            data_list.append(data)
        with open(self.file_name, "w") as file:
            json.dump(data_list, file)

    def read(self):
        """Read the data from the file

        Returns:
        list: a list of data items
        """
        with open(self.file_name, "r") as file:
            return json.load(file)

    def update(self, index, data):
        """Update a data item

        Arguments:
        index (int): the index of the data item to be updated
        data (dict): the updated data
        """
        data_list = self.read()
        data_list[index] = data
        with open(self.file_name, "w") as file:
            json.dump(data_list, file)

    def delete(self, index):
        """Delete a data item

        Arguments:
        index (int): the index of the data item to be deleted
        """
        data_list = self.read()
        data_list.pop(index)
        with open(self.file_name, "w") as file:
            json.dump(data_list, file)
