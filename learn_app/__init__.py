from logging.config import fileConfig

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def init_app():
    """Execute app initialization code"""

    fileConfig("logging.cfg")
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db = SQLAlchemy()
    db.init_app(app)

    return app, db
