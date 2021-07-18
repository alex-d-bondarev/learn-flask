from flask import json, request

from learn_app.main import app, db
from learn_app.test_flow.models.delay import Delay


@app.route("/delay", methods=["GET", "PUT"])
def get_delay():
    """Get processing delay

    :return:
    """
    default_delay = {
        "max_delay": 3000,
        "random": True,
    }

    if request.method == "GET":
        json_body = json.dumps(default_delay)
        return app.response_class(response=json_body, status=200)
    else:
        new_delay = Delay(
            max_delay=default_delay["max_delay"], random=default_delay["random"]
        )
        db.session.add(new_delay)
        return app.response_class(status=204)
