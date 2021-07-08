"""
Application entry point
"""

import datetime
from logging.config import fileConfig

from flask import Flask, g, request
from markupsafe import escape

from learn_app.http_code_response import make_http_code_response_with_status
from learn_app.request_logger import RequestLogger

fileConfig("logging.cfg")
app = Flask(__name__)


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
    http_code = escape(request.args.get("http_code"))
    app.logger.info(f"Processing http code {http_code}")
    json_body, http_status = make_http_code_response_with_status(http_code)
    return app.response_class(
        response=json_body, status=http_status, mimetype="application/json"
    )


if __name__ == "__main__":
    app.run()
