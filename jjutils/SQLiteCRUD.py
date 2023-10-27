import sqlite3

class SQLiteCRUD:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            return True
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")
            return False

    def create_table(self, table_name, columns):
        try:
            if self.connection:
                cursor = self.connection.cursor()
                column_str = ', '.join(columns)
                create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_str})"
                cursor.execute(create_table_query)
                self.connection.commit()
                return True
            else:
                print("Database connection is not established.")
                return False
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            return False

    def insert_data(self, table_name, data):
        try:
            if self.connection:
                cursor = self.connection.cursor()
                placeholders = ', '.join(['?'] * len(data))
                insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
                cursor.execute(insert_query, data)
                self.connection.commit()
                return True
            else:
                print("Database connection is not established.")
                return False
        except sqlite3.Error as e:
            print(f"Error inserting data: {e}")
            return False

    def select_data(self, table_name, condition=None):
        try:
            if self.connection:
                cursor = self.connection.cursor()
                if condition:
                    select_query = f"SELECT * FROM {table_name} WHERE {condition}"
                else:
                    select_query = f"SELECT * FROM {table_name}"
                cursor.execute(select_query)
                return cursor.fetchall()
            else:
                print("Database connection is not established.")
                return []
        except sqlite3.Error as e:
            print(f"Error selecting data: {e}")
            return []

    def update_data(self, table_name, data, condition):
        try:
            if self.connection:
                cursor = self.connection.cursor()
                set_values = ', '.join([f"{key} = ?" for key in data.keys()])
                update_query = f"UPDATE {table_name} SET {set_values} WHERE {condition}"
                cursor.execute(update_query, list(data.values()))
                self.connection.commit()
                return True
            else:
                print("Database connection is not established.")
                return False
        except sqlite3.Error as e:
            print(f"Error updating data: {e}")
            return False

    def delete_data(self, table_name, condition):
        try:
            if self.connection:
                cursor = self.connection.cursor()
                delete_query = f"DELETE FROM {table_name} WHERE {condition}"
                cursor.execute(delete_query)
                self.connection.commit()
                return True
            else:
                print("Database connection is not established.")
                return False
        except sqlite3.Error as e:
            print(f"Error deleting data: {e}")
            return False

    def close(self):
        if self.connection:
            self.connection.close()
