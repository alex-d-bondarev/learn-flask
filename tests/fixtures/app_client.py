import pytest

from learn_app.simple_app import app


@pytest.fixture
def client():
    return app.test_client()
