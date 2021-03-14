import pytest

from learn_app.simple_app import app


@pytest.fixture
def test_client():
    return app.test_client()


@pytest.fixture
def app_context():
    return app.app_context()
