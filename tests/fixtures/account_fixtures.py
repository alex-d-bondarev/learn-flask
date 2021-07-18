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


@pytest.fixture(scope="function")
@pytest.mark.usefixtures("db_fixture", "test_account")
def create_none_account(db_fixture, test_account):
    """Create Account with 'none' role"""
    db_fixture.session.add(test_account)
    db_fixture.session.commit()


@pytest.fixture(scope="function", autouse=True)
@pytest.mark.usefixtures("db_fixture")
def cleanup_test_account(db_fixture):
    """Cleanup account table after each test

    :param db_fixture:
    """
    yield
    Account.query.delete()
    db_fixture.session.commit()
