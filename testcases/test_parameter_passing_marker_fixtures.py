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