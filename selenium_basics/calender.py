from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

# Set options to keep browser open
chr_options = Options()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

try:
    driver.get("https://www.redbus.in/") # Assuming RedBus based on 'onward_cal'
    driver.maximize_window()
    sleep(4)

    # 1. Split your target date
    select_date = "20-Dec-2022"
    dates = select_date.split("-")
    target_day = dates[0]      # "20"

    # 2. Click to open the calendar
    driver.find_element(By.XPATH, "//*[@role='dialog']").click()
    sleep(1)

    all_days = driver.find_elements(By.XPATH, "//li[contains(@class, 'dateItem')]")

    # 2. Loop through them and click the matching number
    for day in all_days:
        if day.text == target_day:
            day.click()
            print(f"[SUCCESS] Clicked date: {target_day}")
            break

except Exception as e:
    print(f"[ERROR] Calendar selection failed: {e}")

