import time   # Changed from trio import sleep to Python's built-in time module
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 

# 1. Fixed the scope typo to "module"
@pytest.fixture(scope="module")
def launch_browser():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    
    # Create the driver instance locally (No global driver needed!)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
    
    # Pass the driver instance directly to the test cases in this module
    yield driver
    
    # Teardown: Safely closes the browser after ALL tests in this module run
    driver.quit()

# 2. First test case
def test_printUrl(launch_browser):
    driver = launch_browser 
    driver.get("https://www.redbus.in/")
    print(f"\n[CURRENT URL] {driver.current_url}")

# 3. Second test case (running on the exact same browser window)
def test_select_date(launch_browser):
    driver = launch_browser
    select_date = "20-Dec-2022"
    dates = select_date.split("-")
    target_day = dates[0]      # "20"

    # 2. Click to open the calendar
    driver.find_element(By.XPATH, "//*[@role='dialog']").click()
    time.sleep(1)

    all_days = driver.find_elements(By.XPATH, "//li[contains(@class, 'dateItem')]")

    # Loop through them and click the matching number
    for day in all_days:
        if day.text == target_day:
            day.click()
            print(f"\n[SUCCESS] Clicked date: {target_day}")
            break