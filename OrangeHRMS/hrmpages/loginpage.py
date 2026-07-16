from selenium.webdriver.common.by import By
from hrmhelper.selenium_helper import Selenium_Helper
# Assuming Selenium_Helper is imported correctly here

class LoginPage(Selenium_Helper):
    email_ele = (By.XPATH, "//input[@name='username']")
    password_ele = (By.XPATH, "//input[@name='password']")
    login_ele = (By.XPATH, "//button")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        # Use self. instead of Selenium_Helper. to invoke inherited methods
        self.webelement_enter(self.email_ele, username)
        self.webelement_enter(self.password_ele, password)
        self.webelement_click(self.login_ele)