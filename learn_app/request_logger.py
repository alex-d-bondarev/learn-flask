"""
Request logger
"""
import datetime
from logging.config import fileConfig

from flask import g, request

fileConfig("logging.cfg")


def log_request_details(app, response):
    """Log request details. Credit to
    https://dev.to/rhymes/logging-flask-requests-with-colors-and-structure--7g1

    :param response:
    """
    duration = datetime.datetime.now() - g.start
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    host = request.host.split(":", 1)[0]
    args = dict(request.args)
    log_params = _make_dictionary_with_logged_parameters(
        args, duration, host, ip, response
    )
    line = _make_log_text_line(log_params)
    app.logger.info(line)


def _make_dictionary_with_logged_parameters(args, duration, host, ip, response):
    log_params = [
        ("method", request.method),
        ("path", request.path),
        ("status", response.status_code),
        ("duration", duration),
        ("ip", ip),
        ("host", host),
        ("params", args),
    ]
    return log_params


def _make_log_text_line(log_params):
    line_items = []
    for name, value in log_params:
        item = f"{name}={value}"
        line_items.append(item)
    line = " ".join(line_items)
    return line
