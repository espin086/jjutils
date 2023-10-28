import uuid
from jjutils import config
from jjutils.SQLiteCRUD import SQLiteCRUD


# creates the database
database = SQLiteCRUD(config.DATABASE_PATH)
database.connect()

# creating the applicant database
database.create_table(
    table_name=config.TABLE_APPLICANTS["name"],
    columns=config.TABLE_APPLICANTS["columns"],
)

# creating the jobs database
database.create_table(
    table_name=config.TABLE_JOBS["name"], columns=config.TABLE_JOBS["columns"]
)


# inserting data into the applicant database
database.insert_data(
    table_name=config.TABLE_APPLICANTS["name"],
    data=("Julie Doe", "julie@gmail.com"),
)

database.insert_data(
    table_name=config.TABLE_APPLICANTS["name"],
    data=("Nancy Doe", "nancy@gmail.com"),
)

database.insert_data(
    table_name=config.TABLE_APPLICANTS["name"],
    data=("Jackie Doe", "jackie@gmail.com"),
)


# selecting data from the applicant database
result = database.select_data(
    table_name=config.TABLE_APPLICANTS["name"], condition="name='Jane Doe'"
)

# updating data
database.update_data(
    table_name=config.TABLE_APPLICANTS["name"],
    data={"name": "Nancy Doe"},
    condition="id=2",
)

# selecting data from the applicant database
result = database.select_data(
    table_name=config.TABLE_APPLICANTS["name"], condition="name='Nancy Doe'"
)


# deleting data
database.delete_data(
    table_name=config.TABLE_APPLICANTS["name"], condition="id=8.925174422111044e+37"
)
database.delete_data(
    table_name=config.TABLE_APPLICANTS["name"], condition="id=1.0937765334688894e+38"
)

# selecting data from the applicant database
result = database.select_data(table_name=config.TABLE_APPLICANTS["name"])
print(result)
