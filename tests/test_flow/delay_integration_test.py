import pytest

from learn_app.test_flow.models.delay import Delay


def test_delay_can_be_created():
    Delay(max_delay=100, random=False)


@pytest.mark.usefixtures("db_fixture", "test_delay")
def test_delay_is_saved_to_db(db_fixture, test_delay):
    db_fixture.session.add(test_delay)
    db_fixture.session.commit()
    db_delay = Delay.query.all()

    assert len(db_delay) == 1


@pytest.mark.usefixtures("test_client", "db_fixture")
def test_delay_api_exists(test_client, db_fixture):
    Delay.query.delete()
    db_fixture.session.commit()
    response = test_client.get("/delay")
    assert response.status_code == 200