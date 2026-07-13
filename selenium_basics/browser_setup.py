
# toinstall selenium and webdriver-manager, run the following commands in your terminal:
# pip3 install selenium
# pip3 install webdriver-manager
# ==============================================


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
input_element = driver.find_element(By.ID, "input")
wait = input_element.send_keys("demo automation testing").click()
class_name = driver.find_element(By.CLASS_NAME, "LC20lb MBeuO DKV0Md").click()