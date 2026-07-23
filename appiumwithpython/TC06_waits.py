from typing import Dict, Any
import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cap: Dict[str, Any] = {
    "platformName": "Android",
    "automationName": "UIAutomator2",
    "deviceName": "Android",
    "appPackage": "com.google.android.contacts",
    "appActivity": "com.android.contacts.activities.PeopleActivity",
    "noReset": True
}

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=AppiumOptions().load_capabilities(cap)
)
wait = WebDriverWait(driver, 20)
wait1 = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])
try:
    time.sleep(3)

    # Create implicitly_wait Contact
    driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,
        "Create contact"
    ).click()
    driver.implicitly_wait(10)

    # Locate Fluent Wait the element
    ele_cancel = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, '//*[@text="CANCEL"]')))
    ele_cancel.click()

    # First Name
    # 1. Properly close the Explicit Wait statement
    ele_firstname = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("First name")'))
    )
    ele_firstname.send_keys("Lokesh")



finally:
    driver.quit()
