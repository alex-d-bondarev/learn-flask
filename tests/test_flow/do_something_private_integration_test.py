from datetime import datetime, timedelta

import pytest
from flask import json

from learn_app.test_flow.models.do_something import DoSomething


def _calculate_time_delta_between_now_and_db_record(create_admin_account, test_client):
    test_datetime = _make_utc_datetime_now_without_milliseconds()
    json_response, process_id = _make_json_response_and_process_id_from_post(
        create_admin_account, test_client
    )
    db_datetime = _query_by_time_from_db(process_id)
    return db_datetime - test_datetime


def _make_json_response_and_process_id_from_post(create_admin_account, test_client):
    response = _post_do_something_for_account(create_admin_account, test_client)
    json_response = json.loads(response.data)
    process_id = json_response["process_id"]
    return json_response, process_id


def _make_utc_datetime_now_without_milliseconds():
    return datetime.utcnow().replace(microsecond=0)


def _post_do_something_for_account(account, test_client):
    do_something_data = {"by_name": account.name}
    response = test_client.post("/do_something_private", data=do_something_data)
    return response


def _query_by_time_from_db(process_id):
    db_do_something = DoSomething.query.filter_by(id=process_id).first()
    db_datetime = db_do_something.by_time
    return db_datetime


def _response_and_json_from_get_do_something(test_client, id):
    response = test_client.get(f"/do_something_private/{id}")
    json_response = json.loads(response.data)
    return json_response, response


def test_do_something_private_has_model():
    DoSomething(by_name="no one", by_time=datetime.utcnow())


@pytest.mark.usefixtures("db_fixture")
def test_do_something_save_to_db(db_fixture):
    do_something = DoSomething(by_name="no one", by_time=datetime.utcnow())
    db_fixture.session.add(do_something)
    db_fixture.session.commit()
    db_do_something = DoSomething.query.all()

    assert len(db_do_something) == 1


@pytest.mark.usefixtures("test_client")
def test_post_do_something_api_exists(test_client):
    response = test_client.post("/do_something_private")
    json_response = json.loads(response.data)

    assert response.status_code == 400
    assert json_response["message"] == "'by_name' parameter not found"


@pytest.mark.usefixtures("test_client")
def test_post_do_something_private_needs_user(test_client):
    do_something_data = {"by_name": "no such name"}
    response = test_client.post("/do_something_private", data=do_something_data)
    json_response = json.loads(response.data)

    assert response.status_code == 404
    assert json_response["message"] == "Account Not Found"


@pytest.mark.usefixtures("create_none_account", "test_client")
def test_account_exists_but_none_role_is_forbidden(create_none_account, test_client):
    response = _post_do_something_for_account(create_none_account, test_client)
    json_response = json.loads(response.data)

    assert response.status_code == 403
    assert json_response["message"] == "Not enough permissions"


@pytest.mark.usefixtures("create_user_account", "test_client")
def test_user_role_is_accepted(create_user_account, test_client):
    response = _post_do_something_for_account(create_user_account, test_client)

    assert response.status_code == 202


@pytest.mark.usefixtures("create_admin_account", "test_client")
def test_user_admin_is_accepted(create_admin_account, test_client):
    response = _post_do_something_for_account(create_admin_account, test_client)

    assert response.status_code == 202


@pytest.mark.usefixtures("create_admin_account", "test_client")
def test_do_something_is_saved_to_db(create_admin_account, test_client):
    _post_do_something_for_account(create_admin_account, test_client)
    db_do_something = DoSomething.query.filter_by(
        by_name=create_admin_account.name
    ).first()

    assert db_do_something is not None


@pytest.mark.usefixtures("create_admin_account", "test_client")
def test_do_something_returns_id(create_admin_account, test_client):
    json_response, process_id = _make_json_response_and_process_id_from_post(
        create_admin_account, test_client
    )
    db_do_something = DoSomething.query.filter_by(id=process_id).first()

    assert db_do_something is not None
    assert json_response["status"] == "processing"


@pytest.mark.usefixtures("test_client")
def test_get_do_something_with_incorrect_id(test_client):
    json_response, response = _response_and_json_from_get_do_something(test_client, 0)

    assert response.status_code == 404
    assert json_response["message"] == "Process Not Found"


@pytest.mark.usefixtures("create_admin_account", "test_client")
def test_get_do_something_with_correct_id(create_admin_account, test_client):
    json_response, process_id = _make_json_response_and_process_id_from_post(
        create_admin_account, test_client
    )
    _, response = _response_and_json_from_get_do_something(test_client, process_id)

    assert response.status_code == 200


@pytest.mark.usefixtures("create_admin_account", "test_client")
def test_do_something_has_different_delta_for_default(
    create_admin_account, test_client
):
    one_second = timedelta(seconds=1)

    time_delta_1 = _calculate_time_delta_between_now_and_db_record(
        create_admin_account, test_client
    )
    time_delta_2 = _calculate_time_delta_between_now_and_db_record(
        create_admin_account, test_client
    )
    time_delta_3 = _calculate_time_delta_between_now_and_db_record(
        create_admin_account, test_client
    )

    assert (
        time_delta_1 > one_second
        or time_delta_2 > one_second
        or time_delta_3 > one_second
    )


@pytest.mark.usefixtures("db_fixture", "test_client")
def test_do_something_is_still_processing_when_future_by_time(db_fixture, test_client):
    one_hour = timedelta(seconds=3600)

    do_something = DoSomething(
        by_name="Mr Hacker", by_time=datetime.utcnow() + one_hour
    )
    db_fixture.session.add(do_something)
    db_fixture.session.commit()

    json_response, _ = _response_and_json_from_get_do_something(
        test_client, do_something.id
    )

    assert json_response["status"] == "processing"
