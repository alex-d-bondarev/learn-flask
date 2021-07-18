import pytest
from flask import json

from learn_app.test_flow.models.delay import Delay

DEFAULT_MAX_DELAY = 3000
DEFAULT_RANDOM = True


def _delay_response_is_default(test_client):
    json_response = _get_delay_as_json(test_client)
    assert json_response["max_delay"] == DEFAULT_MAX_DELAY
    assert json_response["random"] == DEFAULT_RANDOM


def _get_delay_as_json(test_client):
    response = test_client.get("/delay")
    json_response = json.loads(response.data)
    return json_response


def _delete_all_delays_from_db(db_fixture):
    Delay.query.delete()
    db_fixture.session.commit()


def test_delay_can_be_created():
    Delay(max_delay=100, random=False)


@pytest.mark.usefixtures("db_fixture", "test_delay")
def test_delay_is_saved_to_db(db_fixture, test_delay):
    db_fixture.session.add(test_delay)
    db_fixture.session.commit()
    db_delay = Delay.query.all()

    assert len(db_delay) == 1


@pytest.mark.usefixtures("test_client")
def test_delay_api_exists(test_client):
    response = test_client.get("/delay")
    assert response.status_code == 200


@pytest.mark.usefixtures("test_client", "db_fixture")
def test_empty_delay_shows_random_3000(test_client, db_fixture):
    _delete_all_delays_from_db(db_fixture)
    _delay_response_is_default(test_client)


@pytest.mark.usefixtures("test_client")
def test_delay_put_command_is_204(test_client):
    response = test_client.put("/delay")
    assert response.status_code == 204


@pytest.mark.usefixtures("test_client", "db_fixture")
def test_delay_put_creates_db_record_if_none(test_client, db_fixture):
    _delete_all_delays_from_db(db_fixture)

    test_client.put("/delay")
    db_delays = Delay.query.all()

    assert len(db_delays) == 1


@pytest.mark.usefixtures("test_client", "db_fixture")
def test_delay_put_creates_default_db_record_if_no_parameters(test_client, db_fixture):
    _delete_all_delays_from_db(db_fixture)
    test_client.put("/delay")
    _delay_response_is_default(test_client)


@pytest.mark.usefixtures("test_client", "db_fixture")
def test_update_max_delay(test_client, db_fixture):
    _delete_all_delays_from_db(db_fixture)

    new_max_delay = 1000
    update_data = {"max_delay": new_max_delay}
    test_client.put("/delay", data=update_data)

    json_response = _get_delay_as_json(test_client)
    assert json_response["max_delay"] == new_max_delay
    assert json_response["random"] == DEFAULT_RANDOM


@pytest.mark.usefixtures("test_client", "db_fixture")
def test_update_delay_random_value(test_client, db_fixture):
    _delete_all_delays_from_db(db_fixture)

    new_random = False
    update_data = {"random": new_random}
    test_client.put("/delay", data=update_data)

    json_response = _get_delay_as_json(test_client)
    assert json_response["max_delay"] == DEFAULT_MAX_DELAY
    assert json_response["random"] == new_random


@pytest.mark.usefixtures("test_client", "db_fixture")
def test_there_is_always_only_1_delay_record(test_client, db_fixture):
    _delete_all_delays_from_db(db_fixture)

    test_client.put("/delay")
    test_client.put("/delay")

    db_delay = Delay.query.all()
    assert len(db_delay) == 1
