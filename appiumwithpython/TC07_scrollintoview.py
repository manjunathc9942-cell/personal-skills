from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cap = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'Android',
    'appPackage': 'com.hmh.api',
    'appActivity': 'com.hmh.api.ApiDemos'
}

url = 'http://localhost:4723'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

# 1. REMOVED implicit wait setup to prevent conflicts.
# 2. Centralize your explicit wait handler.
wait = WebDriverWait(driver, timeout=10)

# Interact with standard initial popups safely using explicit rules
wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//*[@text="Continue"]'))).click()
wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//*[@text="OK"]'))).click()

# Click Views
ele_setting = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//*[@text="Views"]')))
ele_setting.click()

# Scroll down cleanly to target WebView element
webview_el = driver.find_element(
    by=AppiumBy.ANDROID_UIAUTOMATOR,
    value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("WebView"))'
)
webview_el.click()