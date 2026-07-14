# To install selenium and webdriver-manager, run the following commands in your terminal:
# pip3 install selenium webdriver-manager

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # Single correct import path

# Initialize Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 1. LANDING & LOGIN PAGE
    driver.get("https://demo.automationtesting.in/Index.html")
    driver.maximize_window()  # Maximize early so all elements render properly
    
    input_element = driver.find_element(By.ID, "email")
    input_element.send_keys("manjunathc@gmail.com")
    driver.find_element(By.ID, "enterimg").click()

    # 2. REGISTRATION FORM FILLING
    # Give the registration page a brief moment to load elements
    driver.implicitly_wait(5)

    first_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
    first_name.send_keys("Manjunath")
    
    last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    last_name.send_keys("C")
    
    address = driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']")
    address.send_keys("Bangalore")
    
    email_address = driver.find_element(By.XPATH, "//input[@ng-model='EmailAdress']")
    email_address.send_keys("manjunathc@gmail.com")
    
    phone = driver.find_element(By.XPATH, "//input[@ng-model='Phone']")
    phone.send_keys("1234567890")
    
    gender = driver.find_element(By.XPATH, "//input[@value='Male']")
    gender.click()
    
    # Hobbies Checkbox Iteration
    hobbies = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for hobby in hobbies:
        value = hobby.get_attribute("value")
        if value in ["Cricket"]:
            hobby.click()
            
    # 3. INTERACTING WITH SKILLS DROPDOWN
    # Fixed the variable re-assignment bug here
    skills_element = driver.find_element(By.ID, "Skills")
    sel_skills = Select(skills_element)
    sel_skills.select_by_value("Java")

    # Hard freeze for visual verification
    time.sleep(5)

    # 4. BROWSER NAVIGATION STEPS
    print("[INFO] Navigating to W3Schools...")
    driver.get("https://www.w3schools.com/html/html_forms.asp")
    time.sleep(2)

    print("[INFO] Navigating Back to Registration page...")
    driver.back()
    time.sleep(2)

    print("[INFO] Refreshing the page...")
    driver.refresh()
    
    # Re-maximizing/minimizing workflow as specified in your layout
    driver.minimize_window()
    time.sleep(3)
    driver.maximize_window()

    # 5. INTERACTING WITH COUNTRY DROPDOWN
    # Fixed: Removed the line that was overwriting 'country' back to 'Skills'
    country_element = driver.find_element(By.ID, "countries")
    sel_country = Select(country_element)
    sel_country.select_by_visible_text("Select Country")

    # Final hold before closing down browser context
    time.sleep(5)

except Exception as e:
    print(f"[ERROR] Automation run failed due to: {e}")

finally:
    # Always guarantee driver cleanup
    print("[INFO] Teardown: Closing browser session.")
    driver.quit()