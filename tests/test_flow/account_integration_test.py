import pytest

from learn_app.test_flow.models.account import Account


@pytest.mark.usefixtures("test_account_data")
def test_account_model_creation(test_account_data):
    Account(name=test_account_data["name"], number=test_account_data["number"])


@pytest.mark.usefixtures("test_account_data")
def test_account_model_values(test_account_data):
    account = Account(
        name=test_account_data["name"], number=test_account_data["number"]
    )

    assert test_account_data["name"] == account.name, "names should be the same"
    assert test_account_data["number"] == account.number, "numbers should be the same"


@pytest.mark.usefixtures("db_fixture", "test_account")
def test_account_saved_to_db(db_fixture, test_account):
    db_fixture.session.add(test_account)
    db_fixture.session.commit()
    db_accounts = Account.query.filter_by(name=test_account.name).all()
    assert len(db_accounts) == 1


@pytest.mark.usefixtures("test_client", "test_account_api_data")
def test_account_patch_not_allowed(test_client, test_account_api_data):
    response = test_client.patch("/account", data=test_account_api_data)

    assert response.status_code == 405


@pytest.mark.usefixtures("test_client", "test_account_api_data")
def test_account_post_new_record(test_client, test_account_api_data):
    response = test_client.post("/account", data=test_account_api_data)
    db_accounts = Account.query.filter_by(name=test_account_api_data["name"]).all()
    Account.query.filter_by(name=test_account_api_data["name"]).delete()

    assert response.status_code == 201
    assert len(db_accounts) == 1
