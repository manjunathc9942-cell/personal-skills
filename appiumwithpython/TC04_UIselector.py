from typing import Dict, Any
import time

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# 1. Define Capabilities with the noReset flag included
cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'UIAutomator2',
    'deviceName': 'Android',
    'appPackage': 'com.google.android.contacts',
    'appActivity': 'com.android.contacts.activities.PeopleActivity',
    'noReset': True
}

# 2. Target the local Appium Server address
url = 'http://127.0.0.1:4723'

# 3. Initialize the Remote WebDriver session
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

try:
    # Allow the app a moment to fully load
    time.sleep(3)

    # 4. Locate and click the 'Create new contact' button using Accessibility ID
    ele_setting = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Create contact')
    ele_setting.click()

    # Allow time for the contact creation form to render
    time.sleep(2)

    # 5. Locate the 'First name' input field using native UIAutomator string and type text
    ele_text = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("First name")')
    ele_text.send_keys("Lokesh")

    # Brief pause to visually confirm the input before finishing
    time.sleep(2)

finally:
    # 6. Tear down the session to close the application cleanly
    driver.quit()