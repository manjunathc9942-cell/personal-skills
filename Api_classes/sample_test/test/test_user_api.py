import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    """Initializes the custom API Client once per module test run."""
    return APIClient()

def test_get_users(api_client):
    """Validates that fetching users returns a successful list of entries."""
    response = api_client.get("users")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0