"""Create response for http code"""
from flask import jsonify
from markupsafe import escape


def make_http_code_response(http_code):
    """Create http response in json style

    :param http_code:
    :return:
    """

    response = {'code': http_code}

    return jsonify(response)
