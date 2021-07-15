from logging.config import fileConfig

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def init_app():
    """Execute app initialization code"""

    fileConfig("logging.cfg")
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    return app


def init_app_with_db():
    app = init_app()

    db = SQLAlchemy()
    # db.init_app(app)

    # app.app_context().push()
    # db.create_all()

    return app, db
