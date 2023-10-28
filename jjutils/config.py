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
        "id": "TEXT NOT NULL",
        "name": "TEXT NOT NULL",
        "email": "TEXT NOT NULL",
    },
}

TABLE_JOBS = {
    "name": "jobs",
    "columns": {
        "id": "TEXT NOT NULL",
        "salary": "INTEGER",
        "position": "TEXT",
        "description": "TEXT",
    },
}
