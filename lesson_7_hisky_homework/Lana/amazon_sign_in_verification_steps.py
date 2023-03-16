# from selenium.webdriver.common.by import By
# from pages.base_page import Page
from behave import given, when, then


@when('Click Amazon Orders link')
def click_amazon_orders_link(context):
    context.app.header.click_returns_and_orders()


@then('Verify Sign In page is opened')
def verify_sign_in_page_opens(context):
    context.app.sign_in.verify_sign_in_opens()
    print('Sign in page opened')