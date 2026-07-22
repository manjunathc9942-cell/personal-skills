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

driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Gallery"]').click()
driver.find_element(by=AppiumBy.XPATH, value='//*[@text="1. Photos"]').click()

# Scroll to the right end of the horizontal carousel/gallery
driver.find_element(
    by=AppiumBy.ANDROID_UIAUTOMATOR,
    value='new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToEnd(5)'
)

# Scroll back to the left beginning of the horizontal carousel/gallery
driver.find_element(
    by=AppiumBy.ANDROID_UIAUTOMATOR,
    value='new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToBeginning(5)'
)

# Scroll horizontally until a specific text or image element appears
target_photo = driver.find_element(
    by=AppiumBy.ANDROID_UIAUTOMATOR,
    value='new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollIntoView(new UiSelector().text("Target Photo Name"))'
)
target_photo.click()