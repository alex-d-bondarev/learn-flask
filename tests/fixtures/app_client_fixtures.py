import pytest

from learn_app.main import app


@pytest.fixture(scope="session")
def test_client():
    """Get app client for tests

    :return:
    """
    return app.test_client()


@pytest.fixture(scope="session")
def app_context():
    """Get app context for tests

    :return:
    """
    return app.app_context()
