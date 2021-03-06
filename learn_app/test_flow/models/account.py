from learn_app import db


class Account(db.Model):
    """Account CRUD"""

    __tablename__ = "accounts"

    id = db.Column(name="id", type_=db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(name="name", type_=db.String(20), unique=True, nullable=False)

    number = db.Column(name="number", type_=db.Integer, unique=False, nullable=False)

    role = db.Column(
        name="role", type_=db.String(20), unique=False, nullable=False, default="none"
    )

    def __init__(self, name, number, role="none"):
        self.name = name
        self.number = number
        self.role = role
