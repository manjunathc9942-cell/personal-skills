from typing import Dict, Any
from appium import webdriver
from appium.options.android import UiAutomator2Options

# 1. Define capabilities with proper appium: prefixes
cap: Dict[str, Any] = {
    'platformName': 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:deviceName': 'Android',
    'appium:appPackage': 'com.android.settings',
    'appium:appActivity': 'com.android.settings.Settings',
    "appium:platfromversion": "17",
}

# Load them into Appium Options (Appium 2.0+ standard)
options = UiAutomator2Options().load_capabilities(cap)

# 2. Corrected port to the default 4723 (unless you deliberately changed it)
url = 'http://localhost:4723'

# 3. Completed line 16 from your image to initialize the session
driver = webdriver.Remote(url, options=options)