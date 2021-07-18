from flask import json, request

from learn_app.main import app


@app.route("/do_something_private", methods=["POST"])
def do_something_private():
    """Simulate some processing on backend

    :return:
    """
    req_form = request.form

    if req_form.get("by_name") is not None:
        return _respond_with_by_name()
    else:
        return _respond_without_parameters()


def _respond_with_by_name():
    json_body = json.dumps({"message": "User Not Found"})
    return app.response_class(response=json_body, status=404)


def _respond_without_parameters():
    json_body = json.dumps({"message": "'by_name' parameter not found"})
    return app.response_class(response=json_body, status=400)
