import json

import pytest

from learn_app.test_flow.models.account import Account


def create_account(test_account_api_data, test_client):
    """Create account using given data and client

    :param test_account_api_data:
    :param test_client:
    :return:
    """
    response = test_client.post("/account", data=test_account_api_data)
    return response


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
    response = create_account(test_account_api_data, test_client)
    db_accounts = Account.query.filter_by(name=test_account_api_data["name"]).all()

    assert response.status_code == 201
    assert len(db_accounts) == 1


@pytest.mark.usefixtures("test_client", "test_account_api_data")
def test_account_update_record(test_client, test_account_api_data):
    new_number = 99
    create_account(test_account_api_data, test_client)
    test_account_api_data["number"] = new_number
    response = test_client.put("/account", data=test_account_api_data)
    db_account = Account.query.filter_by(name=test_account_api_data["name"]).first()

    assert response.status_code == 204
    assert db_account.number == new_number


@pytest.mark.usefixtures("test_client", "test_account_api_data")
def test_account_delete_record(test_client, test_account_api_data):
    create_account(test_account_api_data, test_client)
    response = test_client.delete("/account", data=test_account_api_data)
    db_accounts = Account.query.filter_by(name=test_account_api_data["name"]).all()

    assert response.status_code == 204
    assert len(db_accounts) == 0


@pytest.mark.usefixtures("test_client", "test_account_api_data")
def test_get_account_record(test_client, test_account_api_data):
    create_account(test_account_api_data, test_client)
    account_name = test_account_api_data["name"]
    response = test_client.get(f"/account/{account_name}", content_type="html/text")
    json_response = json.loads(response.data)

    assert response.status_code == 200
    assert json_response["name"] == account_name
    assert json_response["number"] == test_account_api_data["number"]
    assert json_response["role"] == test_account_api_data["role"]
