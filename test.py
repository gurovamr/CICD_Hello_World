import pytest
from app import app


@pytest.fixture   # -> Sets up a test client to simulate HTTP requests
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_app_is_working(client): # -> send a GET request to the root /
    response = client.get('/')
    assert response.status_code == 200 # -> (status code OK)
    assert b"Hello from version 2." in response.data
