import pytest


@pytest.mark.usefixtures("client")
def test_index(client):
    response = client.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Index Page"


@pytest.mark.usefixtures("client")
def test_hello(client):
    response = client.get("/hello", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"


@pytest.mark.usefixtures("client")
def test_about(client):
    response = client.get("/about", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"The about page"


@pytest.mark.usefixtures("client")
def test_print_text(client):
    test_text = "unit_test"
    response = client.get(f"/print/{test_text}", content_type="html/text")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == f"Given text {test_text}"


@pytest.mark.usefixtures("client")
def test_translate_http_code(client):
    test_code = "200"
    response = client.get(
        "/translate", query_string=dict(http_code=test_code), content_type="html/text"
    )

    assert response.status_code == 200
    assert response.data.decode("utf-8") == f"Given http code is {test_code}"
