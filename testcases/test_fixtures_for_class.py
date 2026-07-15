import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 

# 1. Define your Class-Scoped Fixture using the 'request' parameter
@pytest.fixture(scope="class")
def launchbrowserclass(request):
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    
    # Dynamically bind the driver instance to the requesting test class (self)
    driver_instance = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=chr_options
    )
    request.cls.driver = driver_instance
    
    yield
    
    # Teardown: Quit the browser after all tests in the class are done
    request.cls.driver.quit()


# 2. Inject the fixture into your class and use self.driver
@pytest.mark.usefixtures("launchbrowserclass")
class Test_Redbus:
    
    def test_entertheURL(self):
        # Access the browser via self.driver
        self.driver.get("https://www.redbus.in/")
        print(f"\nOpened URL: {self.driver.current_url}")
        
    def test_printCurrentTitle(self):
        # We can still use self.driver in subsequent tests inside the same class!
        print(f"Page Title is: {self.driver.title}")