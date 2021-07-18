import pytest

from learn_app.test_flow.models.account import Account


def _save_account_to_db_and_return_its_model(db_fixture, none_account):
    db_fixture.session.add(none_account)
    db_fixture.session.commit()
    return none_account


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
@pytest.mark.usefixtures("db_fixture")
def create_none_account(db_fixture):
    """Create Account with 'none' role"""
    none_account = Account(
        name="Mr. None",
        number=000,
        role="none",
    )
    return _save_account_to_db_and_return_its_model(db_fixture, none_account)


@pytest.fixture(scope="function")
@pytest.mark.usefixtures("db_fixture")
def create_user_account(db_fixture):
    """Create Account with 'none' role"""
    user_account = Account(
        name="Mr. User",
        number=444,
        role="user",
    )
    return _save_account_to_db_and_return_its_model(db_fixture, user_account)


@pytest.fixture(scope="function")
@pytest.mark.usefixtures("db_fixture")
def create_admin_account(db_fixture):
    """Create Account with 'none' role"""
    admin_account = Account(
        name="Mr. Admin",
        number=777,
        role="admin",
    )
    return _save_account_to_db_and_return_its_model(db_fixture, admin_account)


@pytest.fixture(scope="function", autouse=True)
@pytest.mark.usefixtures("db_fixture")
def cleanup_test_account(db_fixture):
    """Cleanup account table after each test

    :param db_fixture:
    """
    yield
    Account.query.delete()
    db_fixture.session.commit()
