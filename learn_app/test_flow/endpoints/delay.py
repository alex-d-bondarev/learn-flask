from flask import json, request

from learn_app.main import app


@app.route("/delay", methods=["GET", "PUT"])
def get_delay():
    """Get processing delay

    :return:
    """
    if request.method == "GET":
        default_delay = {
            "max_delay": 3000,
            "random": True,
        }
        json_body = json.dumps(default_delay)
        return app.response_class(response=json_body, status=200)
    else:
        return app.response_class(status=204)
