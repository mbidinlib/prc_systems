from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get(
        "/", headers={"content-type": "text/html; charset=utf-8"})
    assert response.status_code == 200
    assert b"Welcome to PRC Data Check System" in response.content
    response = client.get("/static/css/style3.css")
    assert response.status_code == 200


def test_page_about():
    response = client.get("/page/about",
                          headers={"content-type": "text/html; charset=utf-8"})
    assert response.status_code == 200
    assert b"About" in response.content


def test_releasenote():
    response = client.get("/releasenote",
                          headers={"content-type": "text/html; charset=utf-8"})
    assert response.status_code == 200
    assert b"Release Note" in response.content


def test_download():
    response = client.post("/download", data={"tag": "flower"}, headers={
                           "Content-Type": "application/x-www-form-urlencoded"})
    assert response.status_code == 200
    assert b"Download" in response.content