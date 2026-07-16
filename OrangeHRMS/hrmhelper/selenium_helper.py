from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Selenium_Helper:
    
    def __init__(self, driver):
        self.driver = driver
        
    def webelement_enter(self, locator, text):
        # Optional: You might want to add .clear() before send_keys if typing into an input field
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)
        
    def webelement_click(self, locator):
        # Optimization: Use element_to_be_clickable for clicks to avoid intercept exceptions
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator)).click()