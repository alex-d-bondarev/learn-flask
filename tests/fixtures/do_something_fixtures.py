import pytest

from learn_app.test_flow.models.do_something import DoSomething


@pytest.fixture(scope="function", autouse=True)
@pytest.mark.usefixtures("db_fixture")
def cleanup_do_something(db_fixture):
    """Cleanup account table after each test

    :param db_fixture:
    """
    yield
    DoSomething.query.delete()
    db_fixture.session.commit()