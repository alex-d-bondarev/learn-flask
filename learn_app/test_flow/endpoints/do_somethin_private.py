from flask import json, request

from learn_app.main import app


@app.route("/do_something_private", methods=["POST"])
def do_something_private():
    """Simulate some processing on backend

    :return:
    """
    req_form = request.form

    if req_form.get("by_name") is not None:
        json_body = json.dumps({"message": "User Not Found"})
        return app.response_class(response=json_body, status=404)
    else:
        json_body = json.dumps({"message": "'by_name' parameter not found"})
        return app.response_class(response=json_body, status=400)
