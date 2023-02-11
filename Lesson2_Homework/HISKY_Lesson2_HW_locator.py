from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/Claudia/gitLessons/python-selenium-automation/Lesson2/chromedriver')

# By ID
driver.find_element(By.ID, 'nav-logo-sprites')              #Amazon logo, search by ID
driver.find_element(By.ID, 'continue')                      #Continue button, search by ID
driver.find_element(By.ID, 'auth-fpp-link-bottom')          #Forgot your password, search by ID
driver.find_element(By.ID, 'ap-other-signin-issues-link')   #Other issues with Sign-In link, search by ID
driver.find_element(By.ID, 'createAccountSubmit')           #Create your Amazon account button

# By xPath, class
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")        #Need help?, by class

# By Xpath, tag and attribute
driver.find_element(By.XPATH, "//*[@id='nav-logo-sprites']")                #Amazon logo, search by xPath
driver.find_element(By.XPATH, "//*[@id='continue']")                        #Continue button, search by xPath
driver.find_element(By.XPATH, "//*[@id='authportal-main-section']/div[2]/div/div[1]/form/div/div/div/div[3]/div/a/span"          #Need Help?, search by absolute path
driver.find_element(By.XPATH, "//*[@id='auth-fpp-link-bottom']")            #Forgot your password, search by XPATH
driver.find_element(By.XPATH, "//*[@id='createAccountSubmit']")             #Create your amazon account button
driver.find_element(By.XPATH, "//*[@id='legalTextRow']/a[1]")               #*Conditions of use link
driver.find_element(By.XPATH, "//*[@id='legalTextRow']/a[2]")               #*Privacy Notice link

#By xPATH, contains
driver.find_element(By.XPATH, "//a([contains(@href, 'ref=nav_logo')]"))     #Amazon logo, search byXpath and contains a/href
driver.find_element(By.XPATH, "//span[contains(text(), 'Need help')]")      #Need help, search by contains text
driver.find_element(By.XPATH, "//a[contains(@href, 'issues')]")             #Other issues with sign-in, search by contains a/href
driver.find_element(By.XPATH, "//a[contains(@href, 'password?')]")          #Forgot your password, search by contains a/href
driver.find_element(By.XPATH, "//a[contains(@href, 'register?')]")          #Create account button, search by contains a/href
