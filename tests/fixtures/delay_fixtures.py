import pytest

from learn_app.test_flow.models.delay import Delay


@pytest.fixture(scope="session")
def test_delay(test_account_data):
    return Delay(max_delay=50, random=False)


@pytest.fixture(scope="function", autouse=True)
@pytest.mark.usefixtures("db_fixture")
def cleanup_test_delay(db_fixture):
    """Cleanup account table after each test

    :param db_fixture:
    """
    yield
    Delay.query.delete()
    db_fixture.session.commit()
