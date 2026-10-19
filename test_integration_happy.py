"""Unit Tests for the Flask Image Recognition Application"""
# test_integration_happy.py

from io import BytesIO

def test_home_page_success(client):
    """Test that the home page loads successfully with a 200 status code."""
    response = client.get("/")

    # Check that the server responded successfully
    assert response.status_code == 200, (
        f"Expected status code 200, but got {response.status_code}"
    )

    # Optional: Check that key content or title appears in the HTML response
    assert b"Welcome" in response.data or b"Sign" in response.data, (
        "Home page response data did not contain expected content."
    )


def test_successful_prediction(client):
    """Test the successful image upload and prediction."""
    # Create a mock image file with minimal valid content
    img_data = BytesIO(b"fake_image_data")
    img_data.name = "test.jpg"

    # Simulate a file upload to the correct prediction endpoint
    response = client.post(
        "/prediction",  # Correct route for prediction
        data={"file": (img_data, img_data.name)},
        content_type="multipart/form-data"
    )

    # Assertions
    assert response.status_code == 200
    assert b"Prediction" in response.data  # Modify this check based on your output
