import pytest


@pytest.fixture
def test_account():
    """Get app context for tests

    :return:
    """
    return {"id": 9999,
            "name": "Mr. Test",
            "number": 42}
