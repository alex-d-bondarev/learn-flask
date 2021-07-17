from logging.config import fileConfig

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
fileConfig("logging.cfg")
app = Flask(__name__)


def init_app():
    """Execute app initialization code"""
    app.config.from_pyfile('config.py')
    init_db()

    return app, db


def init_db():
    """Connect and setup DB"""
    db.init_app(app)
    app.app_context().push()
    init_db_tables()


def init_db_tables():
    """Create tables based on imported models"""
    from learn_app.test_flow.models.account import Account
    db.create_all()
    db.session.commit()
