import pytest
from server import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to My Flask App' in response.data  # Adjust the expected content as needed

def test_not_found(client):
    response = client.get('/non-existent-page')
    assert response.status_code == 404