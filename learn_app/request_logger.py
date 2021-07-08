"""
Request logger
"""
import datetime
from logging.config import fileConfig

from flask import g, request

fileConfig("logging.cfg")


class RequestLogger:
    """Request logger"""

    def __init__(self):
        self.ip = request.headers.get("X-Forwarded-For", request.remote_addr)
        self.host = request.host.split(":", 1)[0]
        self.args = dict(request.args)
        self.duration = 0
        self.log_params_dict = ""
        self.log_line = ""

    def log_request_details(self, app, response):
        """Log request details. Credit to
        https://dev.to/rhymes/logging-flask-requests-with-colors-and-structure--7g1

        :param response:
        """
        self._measure_request_duration()
        self._collect_parameters_to_log(response)
        self._generate_log_line_from_collected_parameters()
        app.logger.info(self.log_line)

    def _measure_request_duration(self):
        self.duration = datetime.datetime.now() - g.start

    def _collect_parameters_to_log(self, response):
        self.log_params_dict = [
            ("method", request.method),
            ("path", request.path),
            ("status", response.status_code),
            ("duration", self.duration),
            ("ip", self.ip),
            ("host", self.host),
            ("params", self.args),
        ]

    def _generate_log_line_from_collected_parameters(self):
        line_items = []
        for name, value in self.log_params_dict:
            item = f"{name}={value}"
            line_items.append(item)
        self.log_line = " ".join(line_items)
