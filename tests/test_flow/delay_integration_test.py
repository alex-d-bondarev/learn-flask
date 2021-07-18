import pytest
from flask import json

from learn_app.test_flow.models.delay import Delay


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
    Delay.query.delete()
    db_fixture.session.commit()
    response = test_client.get("/delay")
    json_response = json.loads(response.data)

    assert json_response["max_delay"] == 3000
    assert json_response["random"]


@pytest.mark.usefixtures("test_client")
def test_delay_put_command_is_204(test_client):
    response = test_client.put("/delay")
    assert response.status_code == 204


# @pytest.mark.usefixtures("test_client")
# def test_delay_update_max_delay(test_client):
#     new_max_delay = 1000
#     update_data = {"max_delay": new_max_delay}
#     response = test_client.put("/delay", data=update_data)
#     response = test_client.get("/delay")
#     json_response = json.loads(response.data)
#
#     assert json_response["max_delay"] == new_max_delay
#     assert json_response["random"]
