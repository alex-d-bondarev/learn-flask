"""
Application entry point
"""

import datetime

from flask import g

from learn_app import init_app
from learn_app.request_logger import RequestLogger

app, db = init_app()


@app.before_request
def start_timer():
    """Start timer for request logger"""
    g.start = datetime.datetime.now()


@app.after_request
def log_request(response):
    """Log request.

    :param response:
    :return:
    """
    RequestLogger().log_request_details(app, response)
    return response


from learn_app.endpoints import about  # noqa: E402, F401
from learn_app.endpoints import hello  # noqa: E402, F401
from learn_app.endpoints import index  # noqa: E402, F401
from learn_app.endpoints import print_text  # noqa: E402, F401
from learn_app.endpoints import translate  # noqa: E402, F401
from learn_app.test_flow.endpoints import account  # noqa: E402, F401
from learn_app.test_flow.endpoints import delay  # noqa: E402, F401
from learn_app.test_flow.endpoints import do_somethin_private  # noqa: E402, F401

if __name__ == "__main__":
    app.run()
