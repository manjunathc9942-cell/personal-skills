from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

# Set options to keep the browser open after execution finishes
chr_options = Options()
chr_options.add_experimental_option("detach", True)

# Initialize Driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), 
    options=chr_options
)

try:
    # 1. Navigation
    driver.get("https://lumapartners.com/events/")
    driver.maximize_window()
    sleep(5)  # Give the initial page plenty of time to fully load
    
    # 2. Hover over "Who We Are" to expand the menu
    print("[INFO] Hovering over 'Who We Are' menu...")
    Who_We_Are = driver.find_element(By.XPATH, "//*[@id='menu-item-20069']")
    action = ActionChains(driver)
    # Perform hover step using a fresh ActionChains instance
    action.move_to_element(Who_We_Are).perform()
    sleep(2)  # Wait for menu dropdown animation to finish

    # 3. Click "Contact Us" from the expanded menu
    print("[INFO] Clicking 'Contact Us'...")
    contact_us = driver.find_element(By.XPATH, "//*[@id='menu-item-11060']")
    contact_us.click()
    sleep(5)  # Wait for the contact page and form to load completely

    # 4. Find the First Name input field on the Contact page
    print("[INFO] Finding the First Name input field...")
    Firstname = driver.find_element(By.XPATH, "//input[@name='first_name']")
    
    # 5. Advanced ActionChain: Hold SHIFT -> Type "Manjunath" -> Release SHIFT
    print("[INFO] Typing 'MANJUNATH' in uppercase using Shift key modifier...")
    ActionChains(driver)\
        .click(Firstname)\
        .key_down(Keys.SHIFT)\
        .send_keys("Manjunath")\
        .key_up(Keys.SHIFT)\
        .send_keys(Keys.TAB)\
        .send_keys("C")\
        .send_keys(Keys.TAB)\
        .perform()

    print("[SUCCESS] Script completed successfully!")

except Exception as e:
    print(f"[ERROR] Automation failed: {e}")

# driver.quit()  # Ensure the browser is closed after execution