import os
import requests

BASE_URL = os.environ.get("APP_URL", "http://localhost:8080")


def test_homepage_loads():
    r = requests.get(BASE_URL)
    assert r.status_code == 200
    assert "Bojan" in r.text


def test_conversion_writes_and_reads_db():
    session = requests.Session()
    page = session.get(BASE_URL)
    token = page.text.split('name="csrf_token" type="hidden" value="')[1].split('"')[0]

    response = session.post(BASE_URL, data={"csrf_token": token, "celsius": "20"})
    assert response.status_code == 200

    assert "68.0" in response.text