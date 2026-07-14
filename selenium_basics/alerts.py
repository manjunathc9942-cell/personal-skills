import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # Single correct import path

# Initialize Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


try:
    driver.get("https://demo.automationtesting.in/Alerts.html")
    driver.maximize_window()  # Maximize early so all elements render properly
    time.sleep(2)  # Wait for the page to load

    print("1. Handling Simple accept Alert")
    driver.find_element(By.ID,'OKTab').click()
    time.sleep(2)  # Wait for the alert 
    
    driver.switch_to.alert.accept()  # Accept the alert
    time.sleep(2)  # Wait after accepting the alert 

    print("2. Handling Confirm Alert")
    driver.find_element(By.XPATH,"//a[@href='#CancelTab']").click()
    time.sleep(2)  # Wait for the tab to load
    driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
    time.sleep(2)  # Wait for the alert
    driver.switch_to.alert.dismiss()  # Dismiss the alert
    time.sleep(2)  # Wait after dismissing the alert

    print("3. Handling Prompt Alert")
    driver.find_element(By.XPATH,"//a[@href='#Textbox']").click()
    time.sleep(2)  # Wait for the tab to load
    driver.find_element(By.XPATH,"//button[@class='btn btn-info']").click()
    time.sleep(2)  # Wait for the alert
    alert = driver.switch_to.alert
    text = driver.switch_to.alert.text
    print(f"Prompt alert text: {text}")
    alert.send_keys("Manjunath")  # Send text to the prompt alert
    time.sleep(2)  # Wait after sending text
    alert.accept()  # Accept the prompt alert
    time.sleep(2)  # Wait after accepting the alert
    print("Prompt alert handled successfully.")

except Exception as e:
    print(f"[ERROR] Automation run failed due to: {e}")

finally:
    # Always guarantee driver cleanup
    print("[INFO] Teardown: Closing browser session.")
    driver.quit()
    