import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Initialize Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 1. LANDING PAGE
    driver.get("https://demo.automationtesting.in/Windows.html")
    driver.maximize_window()
    
    # Save parent window handle
    parent_window = driver.current_window_handle
    print(f"Parent Window: {parent_window}")

    # Click the button that opens the new tab/window
    driver.find_element(By.XPATH, "//a[contains(@href,'http://www.selenium.dev')]").click()

    # Wait for the new window to fully open and register
    time.sleep(3)       

    # Get all window handles
    all_windows = driver.window_handles
    print(f"All Windows: {all_windows}")

    # Switch to the child window
    for window in all_windows:
        if window != parent_window:
            driver.switch_to.window(window)
            print(f"Switched to new window: {window}")
            break
    
    print(f"Current page title after switch: {driver.title}")

    # 2. FIXED: Interacting with the Custom Bootstrap Nav Dropdown
    # Step A: Click to expand the "About" dropdown menu
    about_dropdown = driver.find_element(By.ID, "navbarDropdown")
    about_dropdown.click()
    
    # Brief pause to let the dropdown menu animation complete
    time.sleep(1)

    # Step B: Locate the "Events" option link by its text and click it
    events_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Events')]")
    events_link.click()
    
    print(f"[SUCCESS] Navigated to page: {driver.title}")
    time.sleep(5)  # Pause to visually verify the final page

    driver.close()  # Close the child window
    driver.switch_to.window(parent_window)  # Switch back to the parent window
    print(f"Switched back to parent window: {driver.title}")

finally:
    # Always guarantee driver cleanup
    print("[INFO] Teardown: Closing browser session.")
    driver.quit()