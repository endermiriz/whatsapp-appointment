import os

class Config(object):
    """
    Variables that use os.getenv() function should be changed
    in .env file.
    """
    load_dotenv()