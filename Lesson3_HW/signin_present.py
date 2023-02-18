from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from behave import given, when, then, and
from behave import *



@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('open Amazon orders page')
def openOrdersPage(context):
    context.driver.get('https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first')

@then('verify signin present in page')
def verifySignin(context):
    context.driver.find_element(By.XPATH, "//[h1[contains(text(),'Sign in')]")


@then('verify email input present')
def verifyEmailInput(context):
    context.driver.find_element(By.ID, "ap_email")

