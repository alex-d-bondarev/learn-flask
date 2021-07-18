from datetime import datetime

from learn_app.test_flow.models.SomethingPrivate import SomethingPrivate


def test_do_something_private_has_model():
    SomethingPrivate(by_name="no one", by_time=datetime.utcnow())
