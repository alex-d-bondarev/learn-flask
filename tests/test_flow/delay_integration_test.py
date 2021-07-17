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
