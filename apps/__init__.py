from flask import Flask
from pony.flask import Pony
from pony.orm import Database
from models import *

app = Flask(__name__)
mypony = Pony()

def register_extensions(app):
    db.bind(**app.config['PONY'])
    db.generate_mapping()
    mypony.init_app(app)

def create_app(config):
    app.config.from_object(config)
    register_extensions()

    from apps import routes  # noqa
    return app