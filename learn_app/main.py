"""
Application entry point
"""

import datetime

from flask import g
from markupsafe import escape

from learn_app import init_app_with_db
from learn_app.http_code_response import make_http_code_translation
from learn_app.request_logger import RequestLogger

app, db = init_app_with_db()


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


@app.route("/")
def index():
    """Default url
    :return:
    """
    return "Index Page"


@app.route("/hello")
def hello():
    """Self evident

    :return:
    """
    return "Hello, World!"


@app.route("/about")
def about():
    """Self evident

    :return:
    """
    return "The about page"


@app.route("/print/<text>")
def print_text(text):
    """Print given text

    :return:
    """
    return "Given text %s" % escape(text)


@app.route("/translate")
def translate_http_code():
    """Print given code

    :return:
    """
    return make_http_code_translation()


if __name__ == "__main__":
    app.run()
