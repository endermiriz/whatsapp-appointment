import os


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY")
    PONY = {
        "provider": os.getenv("PROVIDER", "sqlite"),
        "filename": os.getenv("DB_FILENAME", "project.db"),
        "create_db": bool(os.getenv("CREATE_DB", True)),
    }
