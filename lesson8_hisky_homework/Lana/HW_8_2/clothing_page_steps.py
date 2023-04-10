from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages import base_page

CLOTHING_ITEM = 'https://www.amazon.com/black-womens-people-lovers-T-Shirt/dp/B08V7P6SKK/ref=sr_1_3?c=ts&keywords=Novelty+Clothing&qid=1680990697&s=apparel&sr=1-3&ts_id=9103696011'

@given('Open Clothing page')
def open_clothing_page(context):
    context.app.main_page.open_url(CLOTHING_ITEM)


@when('Hover over New Arrivals')
def hover_over_new_arrivals(context):
    context.app.header.hover_over_new_arrivals()
    sleep(4)


@then('Verify that categories appear')
def verify_categories_appear(context):
    obj = context.app.header.verify_categories_appear()

#asserting that the object returned by the function is not none
    assert obj != None
    f'Floating new arrivals\' menu is not displayed'



