import pytest

@pytest.mark.test_marker_demo
def test_marker_demo():
    """
    Test case for the marker demo.
    """
    assert True 

@pytest.mark.test_code 
# Command to run alone: python3 -m pytest -m test_code
def test_code():
    print("Running test code...")   
    assert 5 == 5

@pytest.mark.login
# Command to run multiple: python3 -m pytest -m "login or test_marker_demo"
def test_login():  # Added test_
    print("Running login test...")   
    assert 5 == 5

@pytest.mark.testisnotrequired  
# Command to exclude: python3 -m pytest -m "not testisnotrequired"
def test_is_not_required():  # Added test_
    print("Running test code...") 
    print("failure")  
    assert 4 == 4

@pytest.mark.testisnotrequired2
def test_is_not_required2():  # if the don't want ot run the multiple test cases, then use the below command
    # Command to exclude: python3 -m pytest -m "not testisnotrequired or testisnotrequired2"
    print("Running test code...") 
    print("failure")  
    assert 4 == 4


@pytest.mark.xfail  # if the test case is expected to fail, then use this marker. It will not be counted as a failure in the test report.
def test_failurecases():
    print("Running xfail test...") 
    assert 4 == 4





#note: -v will use to see the test case name in the report. how the command to run the test cases with markers: python3 -m pytest -v -m "test_marker_demo or test_code"