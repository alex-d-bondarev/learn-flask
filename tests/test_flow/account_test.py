import pytest

from learn_app.test_flow.account import Account


@pytest.mark.usefixtures("test_account_data")
def test_account_model_creation(test_account_data):
    Account(id=test_account_data["id"],
            name=test_account_data["name"],
            number=test_account_data["number"])


@pytest.mark.usefixtures("test_account")
def test_account_model_values(test_account_data):
    account = Account(id=test_account_data["id"],
                      name=test_account_data["name"],
                      number=test_account_data["number"])

    assert test_account_data["id"] == account.id, \
        "ids should be the same"
    assert test_account_data["name"] == account.name, \
        "names should be the same"
    assert test_account_data["number"] == account.number, \
        "numbers should be the same"
