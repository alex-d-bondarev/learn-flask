import pytest

from learn_app import init_app_with_db
from learn_app.test_flow.account import Account


@pytest.mark.usefixtures("test_account_data")
def test_account_model_creation(test_account_data):
    Account(name=test_account_data["name"],
            number=test_account_data["number"])


@pytest.mark.usefixtures("test_account_data")
def test_account_model_values(test_account_data):
    account = Account(name=test_account_data["name"],
                      number=test_account_data["number"])

    assert test_account_data["name"] == account.name, \
        "names should be the same"
    assert test_account_data["number"] == account.number, \
        "numbers should be the same"


@pytest.mark.usefixtures("test_account")
def test_account_saved_to_db(test_account):
    _, db = init_app_with_db()
    db.session.add(test_account)
    db.session.commit()
    db_accounts = Account.query.filter_by(name=test_account.name).all()
    assert db_accounts.len == 1
