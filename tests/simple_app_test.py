"""Test simple_app.py"""
import pytest
from flask import json


@pytest.mark.usefixtures("test_client")
def test_index(test_client):
    response = test_client.get("/", content_type="html/text")

    assert response.content_type == "text/html; charset=utf-8"
    assert response.status_code == 200
    assert response.data == b"Index Page"


@pytest.mark.usefixtures("test_client")
def test_hello(test_client):
    response = test_client.get("/hello", content_type="html/text")

    assert response.content_type == "text/html; charset=utf-8"
    assert response.status_code == 200
    assert response.data == b"Hello, World!"


@pytest.mark.usefixtures("test_client")
def test_about(test_client):
    response = test_client.get("/about", content_type="html/text")

    assert response.content_type == "text/html; charset=utf-8"
    assert response.status_code == 200
    assert response.data == b"The about page"


@pytest.mark.usefixtures("test_client")
def test_print_text(test_client):
    test_text = "unit_test"
    response = test_client.get(f"/print/{test_text}", content_type="html/text")

    assert response.content_type == "text/html; charset=utf-8"
    assert response.status_code == 200
    assert response.data.decode("utf-8") == f"Given text {test_text}"


@pytest.mark.usefixtures("test_client")
def test_translate_http_code(test_client):
    test_code = "200"
    response = test_client.get(
        "/translate", query_string=dict(http_code=test_code), content_type="html/text"
    )

    json_response = json.loads(response.data)

    assert response.content_type == "application/json"
    assert response.status_code == 200
    assert json_response["code"] == 200
