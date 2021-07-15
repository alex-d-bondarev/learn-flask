import pytest

from learn_app.test_flow.account import Account


@pytest.fixture
def test_account_data():
    """Get app context for tests

    :return:
    """
    return {"name": "Mr. Test",
            "number": 42}


@pytest.fixture
@pytest.mark.usefixtures("test_account_data")
def test_account(test_account_data):
    return Account(name=test_account_data["name"],
                   number=test_account_data["number"])
