"""Unit Tests for the Flask Image Recognition Application"""
# test_integration_sad.py

import pytest
from app import app

@pytest.fixture
def client():
    """Fixture for the Flask test client."""
    with app.test_client() as instance_client:
        yield instance_client

def test_missing_file(instance_client):
    """Test the prediction route with a missing file."""
    response = instance_client.post("/prediction", data={}, content_type="multipart/form-data")
    assert response.status_code == 200
    assert b"File cannot be processed." in response.data  # Check if the error message is displayed
