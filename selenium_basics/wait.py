from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, time  # Note: Since we import 'sleep' directly, use sleep() instead of time.sleep()

# Initialize Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# =========================================================================
# 📝 STUDY NOTE: THE NO-MIXING RULE (Implicit vs. Explicit Waits)
# =========================================================================
#
# 1. THE CONFLICT: Implicit waits are handled on the browser/driver side, 
#    while Explicit waits are handled locally in your Python code.
# 2. THE PROBLEM: When you mix both, they do not "add up" nicely. Instead,
#    they fight. For example, if an element takes 8 seconds to appear:
#    - Your Explicit wait might tell it to check every 500ms.
#    - The Implicit wait forces the browser to freeze and search for 5 seconds first.
# 3. THE RESULT: This causes highly unpredictable delay times (sometimes 
#    waiting 15+ seconds for a 10-second timeout) or random, flaky crashes.
#
# RULE OF THUMB: Stick entirely to EXPLICIT WAITS (WebDriverWait) for 
# professional frameworks. It is cleaner, faster, and much more reliable.
# =========================================================================

# SETUP EXPLICIT WAIT UTILITY (Standard 10-second timeout max)
wait = WebDriverWait(driver, 10)

try:
    # Navigation
    driver.get("https://demo.automationtesting.in/Register.html")
    driver.maximize_window()

    # FIXED: Changed from 'time.sleep(15)' to 'sleep(15)' to match your import statement
    sleep(15)  # Let the initial page load settle
    
    # Click SwitchTo dropdown using explicit wait
    print("[INFO] Navigating via menu dropdown...")
    driver.find_element(By.XPATH, "//a[contains(text(), 'SwitchTo')]").click()
    driver.implicitly_wait(3)  # Short implicit wait to allow dropdown to render
    
    # Click Frames link
    frames_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Frames')]")))
    frames_link.click()

    # =========================================================================
    # 1. HANDLING SINGLE FRAME WITH EXPLICIT WAIT
    # =========================================================================
    print("1. Handling Single Frame...")
    
    # EXPLICIT WAIT: Checks if the frame exists AND automatically switches into it
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "singleframe")))
    
    # Type text inside the frame
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
    input_box.send_keys("Manjunath")
    
    # Switch back to the main document page context
    driver.switch_to.default_content()
    print("Single frame handled successfully.")

    # =========================================================================
    # 2. HANDLING NESTED FRAMES WITH EXPLICIT WAIT
    # =========================================================================
    print("2. Handling Nested Frames...")
    
    # Click the nested frame tab element
    nested_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Iframe with in an Iframe')]")))
    nested_tab.click()
    
    # EXPLICIT WAIT: Wait for the Outer Frame and switch inside
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@src='MultipleFrames.html']")))
    
    # EXPLICIT WAIT: Wait for the Inner Frame and switch inside
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@src='SingleFrame.html']")))
    
    # Input text inside the inner nested frame
    nested_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
    nested_input.send_keys("Manjunath Nested")
    
    # Switch back to the main document page context completely
    driver.switch_to.default_content()
    print("Nested frames handled successfully.")
    
    # Give it a short pause to visually appreciate your working automation!
    sleep(3)

except Exception as e:
    print(f"[ERROR] Automation run failed due to: {e}")         

finally:    
    print("[INFO] Teardown: Closing browser session.")
    driver.quit()