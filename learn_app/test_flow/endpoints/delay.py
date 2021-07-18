from flask import json

from learn_app.main import app


@app.route("/delay")
def get_delay():
    """Get processing delay

    :return:
    """
    default_delay = {
        "max_delay": 3000,
        "random": True,
    }
    json_body = json.dumps(default_delay)
    return app.response_class(response=json_body, status=200)
