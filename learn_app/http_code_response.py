"""Create response for http code"""
from http.client import responses

from flask import json, jsonify


def make_http_code_response_with_status(http_code):
    """Create http response in json style

    :param http_code:
    :return:
    """
    http_code = int(http_code)
    if http_code in responses:
        return make_successful_json_body(http_code), 200
    else:
        return make_error_json_body(http_code), 404


def make_successful_json_body(http_code):
    """Create json for response body

    :param http_code:
    :return:
    """
    response = {"code": http_code, "name": responses[http_code]}
    jsonify(response)
    return json.dumps(response)


def make_error_json_body(http_code):
    """Create json for response body

    :param http_code:
    :return:
    """
    response = {"code": 404, "name": f"There is no such http code = {http_code}"}
    return json.dumps(response)
