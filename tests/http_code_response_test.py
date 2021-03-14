"""Test http_code_response"""
from http.client import responses

import pytest
from flask import json

from learn_app.http_code_response import make_http_code_response_with_status


@pytest.mark.usefixtures("app_context")
def test_successful_response_code(app_context):
    with app_context:
        response, code = make_http_code_response_with_status(200)
        json_response = json.loads(response)
        assert json_response["code"] == 200


@pytest.mark.usefixtures("app_context")
def test_successful_response_message(app_context):
    with app_context:
        response, code = make_http_code_response_with_status(200)
        json_response = json.loads(response)
        assert json_response["name"] == responses[200]


@pytest.mark.usefixtures("app_context")
def test_error_response_code(app_context):
    with app_context:
        response, code = make_http_code_response_with_status(1)
        json_response = json.loads(response)
        assert json_response["code"] == 404


@pytest.mark.usefixtures("app_context")
def test_error_response_message(app_context):
    with app_context:
        response, code = make_http_code_response_with_status(1)
        json_response = json.loads(response)
        assert json_response["name"] == "There is no such http code = 1"
