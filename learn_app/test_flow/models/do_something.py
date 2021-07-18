from datetime import datetime

from sqlalchemy import DateTime

from learn_app import db


class DoSomething(db.Model):
    """Simulate some action that can be done only by user and admin"""

    __tablename__ = "do_something"

    id = db.Column(name="id", type_=db.Integer, primary_key=True, autoincrement=True)

    by_name = db.Column(
        name="by_name", type_=db.String(20), unique=False, nullable=False
    )

    by_time = db.Column(
        name="by_time",
        type_=DateTime,
        unique=False,
        nullable=False,
        default=datetime.utcnow(),
    )

    def __init__(self, by_name, by_time):
        self.by_name = by_name
        self.by_time = by_time
