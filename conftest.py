"""Pytest configuration for the Flask application."""

import pytest
from app import app  # This imports the Flask app for testing

@pytest.fixture
def client():
    """
    Fixture for the Flask test client.
    - Purpose: Set up a test client for making requests to the Flask app during testing.
    - Usage: Provides a `client` object to use for HTTP request simulations.
    """
    with app.test_client() as client_instance:
        yield client_instance
