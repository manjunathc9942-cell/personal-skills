from typing import Dict, Any
import time

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

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

try:
    time.sleep(3)

    # Create Contact
    driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,
        "Create contact"
    ).click()

    time.sleep(2)

    # First Name
    driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("First name")'
    ).send_keys("Lokesh")

    time.sleep(1)

    # Open Country Picker (+1)
    driver.find_element(
        AppiumBy.XPATH,
        '//android.widget.TextView[@content-desc="United States +1"]'
    ).click()

    time.sleep(2)

    # Scroll until India +91 is found
    india_found = False

    for i in range(20):

        print(f"Scroll : {i+1}")

        india = driver.find_elements(
            AppiumBy.XPATH,
            '//*[contains(@content-desc,"India +91")]'
        )

        if india:
            india[0].click()
            print("India +91 Selected")
            india_found = True
            break

        driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": 100,
                "top": 300,
                "width": 900,
                "height": 1500,
                "direction": "down",
                "percent": 0.8
            }
        )

        time.sleep(1)

    if not india_found:
        raise Exception("India +91 not found")

    time.sleep(2)

    # Select Mobile Type
    driver.find_element(
        AppiumBy.XPATH,
        '//android.widget.EditText[@text="Mobile"]/android.view.View'
    ).click()

    time.sleep(1)

    driver.find_element(
        AppiumBy.XPATH,
        '//android.widget.ScrollView/android.view.View[11]'
    ).click()

    time.sleep(1)

    # Phone Number
    phone = driver.find_element(
        AppiumBy.XPATH,
        '//android.widget.EditText[contains(@text,"+91")]'
    )

    phone.click()
    phone.send_keys("+919654320988")
    driver.press_keycode(66)

    time.sleep(5)

finally:
    driver.quit()