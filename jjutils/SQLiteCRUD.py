import sqlite3
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class SQLiteCRUD:
    """
    SQLite CRUD class for managing SQLite database operations.

    Attributes:
        db_name (str): The name of the SQLite database.
        connection (sqlite3.Connection): The SQLite database connection object.
    """

    def __init__(self, db_name):
        """
        Initialize the SQLiteCRUD with a database name.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = None

    def connect(self):
        """
        Connect to the SQLite database.

        Returns:
            bool: Returns True if connection is successful, otherwise False.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            logging.info(f"Connected to the database: {self.db_name}")
            return True
        except sqlite3.Error as e:
            logging.error(f"Error connecting to the database: {e}")
            return False

    def create_table(self, table_name, columns):
        """
        Create a table in the SQLite database.

        Args:
            table_name (str): The name of the table to create.
            columns (list): A list of column definitions.

        Returns:
            bool: Returns True if table creation is successful, otherwise False.
        """
        try:
            if self.connection:
                cursor = self.connection.cursor()
                column_str = ", ".join(columns)
                create_table_query = (
                    f"CREATE TABLE IF NOT EXISTS {table_name} ({column_str})"
                )
                cursor.execute(create_table_query)
                self.connection.commit()
                logging.info(f"Created table: {table_name}")
                return True
            else:
                logging.warning("Database connection is not established.")
                return False
        except sqlite3.Error as e:
            logging.error(f"Error creating table: {e}")
            return False

    def insert_data(self, table_name, data):
        """
        Insert data into a table in the SQLite database.

        Args:
            table_name (str): The name of the table to insert data into.
            data (tuple): A tuple of data values to be inserted.

        Returns:
            bool: Returns True if data insertion is successful, otherwise False.
        """
        try:
            if self.connection:
                cursor = self.connection.cursor()
                placeholders = ", ".join(["?"] * len(data))
                insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
                cursor.execute(insert_query, data)
                self.connection.commit()
                logging.info(f"Inserted data into table: {table_name}")
                return True
            else:
                logging.warning("Database connection is not established.")
                return False
        except sqlite3.Error as e:
            logging.error(f"Error inserting data: {e}")
            return False

    def select_data(self, table_name, condition=None):
        """
        Select data from a table in the SQLite database.

        Args:
            table_name (str): The name of the table to select data from.
            condition (str, optional): The WHERE clause condition. Defaults to None.

        Returns:
            list: A list of rows selected from the table.
        """
        try:
            if self.connection:
                cursor = self.connection.cursor()
                if condition:
                    select_query = f"SELECT * FROM {table_name} WHERE {condition}"
                else:
                    select_query = f"SELECT * FROM {table_name}"
                cursor.execute(select_query)
                rows = cursor.fetchall()
                logging.info(f"Selected data from table: {table_name}")
                return rows
            else:
                logging.warning("Database connection is not established.")
                return []
        except sqlite3.Error as e:
            logging.error(f"Error selecting data: {e}")
            return []

    def update_data(self, table_name, data, condition):
        """
        Update data in a table in the SQLite database.

        Args:
            table_name (str): The name of the table to update data.
            data (dict): A dictionary of column-value pairs to be updated.
            condition (str): The WHERE clause condition.

        Returns:
            bool: Returns True if data update is successful, otherwise False.
        """
        try:
            if self.connection:
                cursor = self.connection.cursor()
                set_values = ", ".join([f"{key} = ?" for key in data.keys()])
                update_query = f"UPDATE {table_name} SET {set_values} WHERE {condition}"
                cursor.execute(update_query, list(data.values()))
                self.connection.commit()
                logging.info(f"Updated data in table: {table_name}")
                return True
            else:
                logging.warning("Database connection is not established.")
                return False
        except sqlite3.Error as e:
            logging.error(f"Error updating data: {e}")
            return False

    def delete_data(self, table_name, condition):
        """
        Delete data from a table in the SQLite database.

        Args:
            table_name (str): The name of the table to delete data from.
            condition (str): The WHERE clause condition.

        Returns:
            bool: Returns True if data deletion is successful, otherwise False.
        """
        try:
            if self.connection:
                cursor = self.connection.cursor()
                delete_query = f"DELETE FROM {table_name} WHERE {condition}"
                cursor.execute(delete_query)
                self.connection.commit()
                logging.info(f"Deleted data from table: {table_name}")
                return True
            else:
                logging.warning("Database connection is not established.")
                return False
        except sqlite3.Error as e:
            logging.error(f"Error deleting data: {e}")
            return False

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            logging.info("Closed the database connection.")
