from sqlalchemy import Boolean

from learn_app import db


class Delay(db.Model):
    """Per task README"""

    __tablename__ = "delay"

    id = db.Column(name="id", type_=db.Integer, primary_key=True, autoincrement=True)

    max_delay = db.Column(
        name="max_delay", type_=db.Integer, unique=False, nullable=False
    )

    random = db.Column(
        name="random", type_=Boolean, unique=False, nullable=False, default=False
    )

    def __init__(self, max_delay, random):
        self.max_delay = max_delay
        self.random = random
