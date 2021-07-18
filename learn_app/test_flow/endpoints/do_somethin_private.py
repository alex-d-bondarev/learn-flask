from flask import json, request

from learn_app.main import app
from learn_app.test_flow.models.account import Account


@app.route("/do_something_private", methods=["POST"])
def do_something_private():
    """Simulate some processing on backend

    :return:
    """
    req_form = request.form

    if req_form.get("by_name") is not None:
        return _respond_with_by_name(req_form.get("by_name"))
    else:
        return _respond_without_parameters()


def _respond_with_by_name(name):
    account = Account.query.filter_by(name=name).first()
    if account is None:
        json_body = json.dumps({"message": "User Not Found"})
        return app.response_class(response=json_body, status=404)
    else:
        json_body = json.dumps({"message": "Not enough permissions"})
        return app.response_class(response=json_body, status=403)


def _respond_without_parameters():
    json_body = json.dumps({"message": "'by_name' parameter not found"})
    return app.response_class(response=json_body, status=400)
