# test_app.py
import pytest
from app import app  # Import the app instance from app.py

# Use the Flask test client to simulate requests
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    # Simulate a GET request to the homepage
    response = client.get('/')
    assert response.status_code == 200  # Check for a successful response
    assert response.data == b"Hello, World!"  # Check the content of the response

def test_about(client):
    # Simulate a GET request to the about page
    response = client.get('/about')
    assert response.status_code == 200
    assert response.data == b"This is the About Page!"  # Check the content of the response
