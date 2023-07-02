from flask import Flask
from pony.flask import Pony
from pony.orm import Database

app = Flask(__name__)
db = Database()
pony = Pony()

def register_extensions(app):
    pass

def create_app(config):
    app.config.from_object(config)

    from apps import routes  # noqa

    return app