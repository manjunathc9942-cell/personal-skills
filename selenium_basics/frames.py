import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Initialize Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 1. LANDING & NAVIGATION
    driver.get("https://demo.automationtesting.in/Register.html")
    driver.maximize_window()
    time.sleep(2)  # Wait for page load
    
    # Click the "SwitchTo" menu header to expand the dropdown list
    print("[INFO] Navigating via menu dropdown...")
    driver.find_element(By.XPATH, "//a[contains(text(), 'SwitchTo')]").click()
    time.sleep(1)  # Brief pause for dropdown transition
    
    # Click the "Frames" option link inside the expanded menu
    driver.find_element(By.XPATH, "//a[contains(text(), 'Frames')]").click()
    time.sleep(2)  # Wait for the Frames page to load

    # 2. HANDLING SINGLE FRAME
    print("1. Handling Single Frame...")
    # Locate the single iframe and switch context into it
    single_iframe_element = driver.find_element(By.ID, "singleframe")
    driver.switch_to.frame(single_iframe_element)
    
    # Input text inside the frame
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Manjunath")
    time.sleep(1)
    
    # Crucial: Switch back to the main document page context
    driver.switch_to.default_content()
    print("Single frame handled successfully.")

    # 3. HANDLING NESTED FRAMES
    print("2. Handling Nested Frames...")
    # Click the tab to display the nested iframe option
    driver.find_element(By.XPATH, "//a[contains(text(),'Iframe with in an Iframe')]").click()
    time.sleep(1)
    
    # Switch into the Outer Frame
    outer_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
    driver.switch_to.frame(outer_frame)
    
    # Switch into the Inner Frame
    inner_frame = driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")
    driver.switch_to.frame(inner_frame)
    
    # Input text inside the inner nested frame
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Manjunath Nested")
    time.sleep(2)
    
    # Switch back to the main document page context
    driver.switch_to.default_content()
    print("Nested frames handled successfully.")
    
    time.sleep(3)  # Visual verification pause

except Exception as e:
    print(f"[ERROR] Automation run failed due to: {e}")         

finally:    
    # Always guarantee driver cleanup
    print("[INFO] Teardown: Closing browser session.")
    driver.quit()