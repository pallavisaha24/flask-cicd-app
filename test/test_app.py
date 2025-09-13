import pytest
from src.app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_root(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Hello" in res.data

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.data == b"OK"

