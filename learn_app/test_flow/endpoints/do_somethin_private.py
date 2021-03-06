import random
from datetime import datetime, timedelta

from flask import json, request

from learn_app.main import app, db
from learn_app.test_flow.endpoints.delay import calculate_current_delay
from learn_app.test_flow.models.account import Account
from learn_app.test_flow.models.do_something import DoSomething


@app.route("/do_something_private/<id>")
def get_do_something_private(id):
    """Get account with given name as json

    :return:
    """
    db_do_something = DoSomething.query.filter_by(id=id).first()

    if db_do_something is None:
        return _respond_get_not_found()
    else:
        return _respond_get_found(db_do_something)


def _respond_get_found(db_do_something):
    json_response = _prepare_do_something_details_json(db_do_something)
    return app.response_class(response=json_response, status=200)


def _prepare_do_something_details_json(db_do_something):
    status = _calculate_status(db_do_something.by_time)
    response = {"by_time": db_do_something.by_time, "status": status}
    json_response = json.dumps(response)
    return json_response


def _calculate_status(db_time):
    if datetime.utcnow().replace(microsecond=0) > db_time:
        return "done"
    else:
        return "processing"


def _respond_get_not_found():
    response = {"message": "Process Not Found"}
    json_response = json.dumps(response)
    return app.response_class(response=json_response, status=404)


@app.route("/do_something_private", methods=["POST"])
def do_something_private():
    """Simulate some processing on backend

    :return:
    """
    req_form = request.form

    if req_form.get("by_name") is not None:
        return _respond_with_by_name(req_form.get("by_name"))
    else:
        return _respond_parameter_not_found()


def _respond_with_by_name(name):
    account = Account.query.filter_by(name=name).first()
    if account is None:
        return _respond_account_not_found()
    else:
        return _respond_account_found(account)


def _respond_account_found(account):
    if account.role in ["admin", "user"]:
        return _respond_do_something_successfully(account)
    else:
        return _respond_not_enough_permissions()


def _respond_do_something_successfully(account):
    process_id = _save_do_something_to_db(account)
    response = {
        "status": "processing",
        "process_id": process_id,
    }
    json_response = json.dumps(response)
    return app.response_class(response=json_response, status=202)


def _save_do_something_to_db(account):
    delay_time_delta = _calculate_delay_time_delta()
    do_something = DoSomething(
        by_name=account.name, by_time=datetime.utcnow() + delay_time_delta
    )
    db.session.add(do_something)
    db.session.commit()
    return do_something.id


def _calculate_delay_time_delta():
    current_delay = calculate_current_delay()
    delay_seconds = random.randint(1, current_delay["max_delay"])
    return timedelta(seconds=delay_seconds)


def _respond_not_enough_permissions():
    json_body = json.dumps({"message": "Not enough permissions"})
    return app.response_class(response=json_body, status=403)


def _respond_account_not_found():
    json_body = json.dumps({"message": "Account Not Found"})
    return app.response_class(response=json_body, status=404)


def _respond_parameter_not_found():
    json_body = json.dumps({"message": "'by_name' parameter not found"})
    return app.response_class(response=json_body, status=400)
