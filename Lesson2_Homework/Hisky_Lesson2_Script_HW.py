from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

#using the service class to declare the path
service = Service('./chromedriver.exe')     #telling where to look for a webdriver
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')       #telling the driver to open the Amazon webpage

#telling the driver to find the signin arrow and click on it
driver.find_element(By.XPATH, "//*[@id='nav-link-accountList']/span/span").click()

# wait for 3 sec
sleep(3)

#closing the browser
driver.quit()
