from datetime import datetime

import pytest

from learn_app.test_flow.models.do_something import DoSomething


def test_do_something_private_has_model():
    DoSomething(by_name="no one", by_time=datetime.utcnow())


@pytest.mark.usefixtures("db_fixture")
def test_do_something_save_to_db(db_fixture):
    do_something = DoSomething(by_name="no one", by_time=datetime.utcnow())
    db_fixture.session.add(do_something)
    db_fixture.session.commit()
    db_do_something = DoSomething.query.all()

    assert len(db_do_something) == 1


@pytest.mark.usefixtures("test_client")
def test_get_do_something_api_exists(test_client):
    response = test_client.post("/do_something_private")
    assert response.status_code == 400
