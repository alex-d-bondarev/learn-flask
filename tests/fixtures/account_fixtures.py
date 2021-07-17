import pytest

from learn_app.test_flow.models.account import Account


@pytest.fixture(scope="session")
def test_account_data():
    """Get app context for tests

    :return:
    """
    return {"name": "Mr. Test", "number": 42, "role": "none"}


@pytest.fixture(scope="session")
def test_account_api_data():
    """Get app context for tests

    :return:
    """
    return {"name": "Mr. API", "number": 42, "role": "none"}


@pytest.fixture(scope="session")
@pytest.mark.usefixtures("test_account_data")
def test_account(test_account_data):
    return Account(
        name=test_account_data["name"],
        number=test_account_data["number"],
        role=test_account_data["role"],
    )


@pytest.fixture(scope="function", autouse=True)
@pytest.mark.usefixtures("db_fixture", "test_account")
def cleanup_test_account(db_fixture, test_account):
    """Cleanup account table after each test

    :param db_fixture:
    :param test_account:
    """
    yield
    Account.query.delete()
    db_fixture.session.commit()
