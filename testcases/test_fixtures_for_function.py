import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# 1. Cleaned up the spelling to launch_browser
@pytest.fixture(scope="function")
def launch_browser():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    global driver  # Declare the driver as a global variable to be accessible in the test case
    # Create the driver instance locally
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
    
    # Pass the driver instance directly to the test case
    yield driver
    driver.quit()  # This will run after the test case finishes, ensuring the browser is closed
    
    # OPTIONAL TEARDOWN: This line will run automatically after your test finishes!
    # driver.quit()

# 2. Accept the fixture instance as an argument
def test_printUrl(launch_browser):
    # Rename the incoming object reference locally to 'driver'
    driver = launch_browser 
    driver.get("https://www.redbus.in/")
    print(driver.current_url)
    print("Running test code...") 
    print("failure")  
    assert 4 == 3