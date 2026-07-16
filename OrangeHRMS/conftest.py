import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager # <-- Add this import at the top

BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
username = "Admin"
password = "admin123"

@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chrome_option = Options()
    chrome_option.add_experimental_option("detach", True)
    
    # 1. Correct Service syntax and Capital 'C' in Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_option)
    
    # 2. Assign to class (for your tests) AND to node (for the report screenshot hook)
    request.cls.driver = driver
    request.node.driver = driver
    
    # yield driver
    
    # driver.quit()