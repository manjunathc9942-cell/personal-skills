
# toinstall selenium and webdriver-manager, run the following commands in your terminal:
# pip3 install selenium
# pip3 install webdriver-manager
# ==============================================


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")