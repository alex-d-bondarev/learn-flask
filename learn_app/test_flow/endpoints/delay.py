from flask import json, request

from learn_app.main import app, db
from learn_app.test_flow.models.delay import Delay


@app.route("/delay", methods=["GET", "PUT"])
def get_delay():
    """Get processing delay

    :return:
    """
    if request.method == "GET":
        return _get_delay()
    else:
        return _put_delay()


def _put_delay():
    delay_dict = _make_default_delay_dict()
    _update_default_delay_based_on_request(delay_dict)
    _save_delay_to_db(delay_dict)
    return app.response_class(status=204)


def _update_default_delay_based_on_request(default_delay):
    req_form = request.form
    if req_form.get("max_delay") is not None:
        default_delay["max_delay"] = req_form.get("max_delay")
    if req_form.get("random") is not None:
        default_delay["random"] = req_form.get("random").lower() == "true"


def _save_delay_to_db(default_delay):
    db_delay = Delay.query.first()
    if db_delay is None:
        db_delay = Delay(
            max_delay=default_delay["max_delay"], random=default_delay["random"]
        )
    else:
        db_delay.max_delay = default_delay["max_delay"]
        db_delay.random = default_delay["random"]
    db.session.merge(db_delay)
    db.session.commit()


def _get_delay():
    result_delay = calculate_current_delay()
    json_body = json.dumps(result_delay)
    return app.response_class(response=json_body, status=200)


def calculate_current_delay():
    """Calculate current delay based on DB records and default behavior

    :return:
    """
    delay_dict = _make_default_delay_dict()
    db_delay = Delay.query.first()
    result_delay = _prepare_result_delay(db_delay, delay_dict)
    return result_delay


def _prepare_result_delay(db_delay, default_delay):
    if db_delay is None:
        return default_delay
    else:
        return {
            "max_delay": db_delay.max_delay,
            "random": db_delay.random,
        }


def _make_default_delay_dict():
    default_delay = {
        "max_delay": 3,
        "random": True,
    }
    return default_delay
