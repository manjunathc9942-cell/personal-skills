
# toinstall selenium and webdriver-manager, run the following commands in your terminal:
# pip3 install selenium
# pip3 install webdriver-manager

# locators:
# id: driver.find_element(By.ID, "value")
# name: driver.find_element(By.NAME, "value")
# CLASS_NAME: driver.find_element(By.CLASS_NAME, "value")
# TAG_NAME: driver.find_element(By.TAG_NAME, "value")
# LINK_TEXT: driver.find_element(By.LINK_TEXT, "value")
# PARTIAL_LINK_TEXT: driver.find_element(By.PARTIAL_LINK_TEXT, "value")
# CSS_SELECTOR: driver.find_element(By.CSS_SELECTOR, "value")

# xpath locators:
# //tagname[@attribute='value'] | //*[@attribute='value'] 
# //tagname[@attribute='value' and @attribute='value']
# //tagname[@attribute='value' or @attribute='value'] 
# //tagname[contains(@attribute,'value')] 
# //tagname[starts-with(@attribute,'value')] 
# //tagname[text()='value']
# //tagname[contains(text(),'value')] 
# //tagname[starts-with(text(),'value')] 
# //tagname[ends-with(text(),'value')]


# following-sibling: //tagname[@attribute='value']/following-sibling::tagname
# preceding-sibling: //tagname[@attribute='value']/preceding-sibling::tagname

# ==============================================


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Index.html")
input_element = driver.find_element(By.ID, "email")
wait = input_element.send_keys("manjunathc@gmail.com")
driver.find_element(By.ID, "enterimg").click()

first_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
first_name.send_keys("Manjunath")
last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
last_name.send_keys("C")
adress = driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']")
adress.send_keys("Bangalore")
emailadress = driver.find_element(By.XPATH, "//input[@ng-model='EmailAdress']")
emailadress.send_keys("manjunathc@gmail.com")
phone = driver.find_element(By.XPATH, "//input[@ng-model='Phone']")
phone.send_keys("1234567890")
gender = driver.find_element(By.XPATH, "//input[@value='Male']")
gender.click()
hobbies = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for hobby in hobbies:
    value = hobby.get_attribute("value")
    if value in ["Cricket"]:
        hobby.click()
Languages = driver.find_element(By.ID, "msdd").click()
for language in Languages:
    value = language.get_attribute("value")
    if value in ["ENGLISH"]:
        hobby.click()
skills = Select(driver.find_element(By.ID, "Skills"))
skills.select_by_visible_text("Android")
