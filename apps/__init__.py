from flask import Flask
from pony.flask import Pony
from pony.orm import Database


app = Flask(__name__)
db = Database()
mypony = Pony()


def register_extensions(app):
    from apps import routes  # noqa

    db.bind(**app.config["PONY"])
    db.generate_mapping(create_tables=True)
    mypony.init_app(app)


def create_app(config):
    app.config.from_object(config)
    register_extensions(app)
    return app
