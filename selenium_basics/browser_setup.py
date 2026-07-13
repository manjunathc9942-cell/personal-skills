
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
driver.get("https://demo.automationtesting.in/Index.html")
input_element = driver.find_element(By.ID, "email")
wait = input_element.send_keys("manjunathc9942@gmail.com")
driver.find_element(By.ID, "enterimg").click()