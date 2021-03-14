"""Test http_code_response"""
import pytest
from flask import json
from learn_app.http_code_response import *


@pytest.mark.usefixtures("app_context")
def test_make_http_code_response(app_context):
    with app_context:
        response = make_http_code_response(200)
        json_response = json.loads(response.data)
        assert json_response["code"] == 200
