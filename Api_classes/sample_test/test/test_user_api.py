import pytest
from utils.api_client import APIClient


@pytest.fixture(scope="module")
def api_client():
    """Initializes the custom API Client once per module test run."""
    return APIClient()


def test_get_users(api_client):
    """Validates that fetching an existing user returns a successful list of entries."""
    # 1 is a static ID pre-seeded on the mock server, so this will always pass
    responseget = api_client.get("users/1")
    assert responseget.status_code == 200
    assert responseget.json()['id'] == 1


def test_create_users(api_client):
    """Validates user creation payload and mock response."""
    user_data = {
        "name": "prasanth",
        "username": "qa user",
        "email": "test655@gmail.com"
    }

    # 1. Create the user
    response = api_client.post("users", user_data)
    print("POST Response:")
    print(response.json())

    # 2. Verify the mock creation was successful
    assert response.status_code == 201
    assert response.json()['name'] == 'prasanth'
    assert response.json()['username'] == 'qa user'
    assert response.json()['email'] == 'test655@gmail.com'
    assert 'id' in response.json()  # Ensure the mock server generated an ID

    # Note: We omitted the GET request for the newly created ID here.
    # On mock servers like JSONPlaceholder, mock IDs (e.g., ID 11)
    # are not persisted, making a GET request to f"users/{id}" return a 404.