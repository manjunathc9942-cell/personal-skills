import pytest
from conftest import *
from hrmpages.loginpage import LoginPage

@pytest.mark.usefixtures("browser_setup")
class Test_login:

    # 1. Correct class setup configuration using @classmethod and cls
    @classmethod
    def setup_class(cls):
        # The autouse fixture runs right before this, so cls.driver is ready
        cls.driver.get(BaseUrl)
        cls.login_page = LoginPage(cls.driver)

    def test_valid_login(self):
        # Inside test instances, you can now safely call the initialized page object
        self.login_page.login(username, password)