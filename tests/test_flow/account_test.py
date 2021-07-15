import pytest

from learn_app.test_flow.account import Account


@pytest.mark.usefixtures("test_account")
def test_account_model_creation(test_account):
    Account(id=test_account["id"],
            name=test_account["name"],
            number=test_account["number"])
