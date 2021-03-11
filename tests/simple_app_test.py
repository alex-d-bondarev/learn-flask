import pytest


@pytest.mark.usefixtures("client")
def test_index(client):
    response = client.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Index Page"
