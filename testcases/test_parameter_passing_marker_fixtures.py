import pytest

# Approach A: Test Function Parameterization (Runs 3 times)
@pytest.mark.parametrize("name,role", [
    ("Ram", "QA"),
    ("swetha", "dev"),
    ("ravi", "manager")
])
def test_validation(name, role):
    assert name is not None
    assert role is not None


# Approach B: Fixture Parameterization (Runs 2 times because of 2 URLs)
@pytest.fixture(scope="module", params=["www.google.com", "www.redbus.in"])
def val(request):
    # Access the current parameter using request.param
    return request.param

def test_val(val):
    # This test will run twice: once for google, once for redbus!
    assert val is not None
    print(f"\n[TESTING URL] {val}")






#     What are they?
# Marker (@pytest.mark): A label (tag) used to categorize or configure how a test runs. It does not execute setup code.

# Fixture (@pytest.fixture): A resource provider that runs setup code before a test and teardown (cleanup) code after it.

# Where to use them?
# Use Markers for:
# Grouping: Running only specific tests (e.g., pytest -m smoke).

# Skipping: Ignoring tests conditionally (e.g., skip on Windows).

# Expected Fails: Tagging known broken tests (@pytest.mark.xfail).

# Data Loop: Running one test with multiple inputs (@pytest.mark.parametrize).

# Use Fixtures for:
# Browsers: Launching and closing Chrome/Firefox.

# Databases: Opening a connection, inserting test data, and cleaning it up after.

# API Clients: Initializing session headers or authorization tokens.

# Configuration: Loading global settings or .env files.