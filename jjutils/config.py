import logging
import os
from pathlib import Path

# == General Configs ==
LOGGING_LEVEL = logging.info


# == Data Configs ==
CWD_PATH = Path(os.getcwd())

# == Database Configs ==
DATABASE_PATH = CWD_PATH / "data" / "database.db"

TABLE_APPLICANTS = {
    "name": "applicants",
    "columns": {
        "id": "INTEGER NOT NULL",
        "name": "TEXT NOT NULL",
        "email": "TEXT NOT NULL",
    },
}

TABLE_JOBS = {
    "name": "jobs",
    "columns": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "salary": "INTEGER",
        "position": "TEXT",
        "description": "TEXT",
    },
}
