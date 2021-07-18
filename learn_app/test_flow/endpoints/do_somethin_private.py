from datetime import datetime

from flask import json, request

from learn_app.main import app, db
from learn_app.test_flow.models.account import Account
from learn_app.test_flow.models.do_something import DoSomething


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
    _save_do_something_to_db(account)
    return app.response_class(status=202)


def _save_do_something_to_db(account):
    do_something = DoSomething(by_name=account.name, by_time=datetime.utcnow())
    db.session.add(do_something)
    db.session.commit()


def _respond_not_enough_permissions():
    json_body = json.dumps({"message": "Not enough permissions"})
    return app.response_class(response=json_body, status=403)


def _respond_account_not_found():
    json_body = json.dumps({"message": "Account Not Found"})
    return app.response_class(response=json_body, status=404)


def _respond_parameter_not_found():
    json_body = json.dumps({"message": "'by_name' parameter not found"})
    return app.response_class(response=json_body, status=400)
