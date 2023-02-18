from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')



# By CSS
driver.find_element(By.CSS_SELECTOR, '#ap_email')
driver.find_element(By.CSS_SELECTOR, '#ap_password')
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# Conditions of use
driver.find_element(By.CSS_SELECTOR,"#legalTextRow a[href*=condition_of_use]")
#privacy notice
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*=privacy_notice?]")
