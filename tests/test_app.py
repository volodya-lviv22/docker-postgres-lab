import sys
import os

sys.path.append(os.path.abspath("app"))

from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.data == b"OK"


def test_version():
    client = app.test_client()

    response = client.get("/version")

    assert response.status_code == 200
    assert b"v3.0.0" in response.data
