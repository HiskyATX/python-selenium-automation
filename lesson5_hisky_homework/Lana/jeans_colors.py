from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep


OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')
    print(product_id)
  #  sleep(4)

# @when('User Clicks on Desired Item')
# def user_clicks_desired_item(context):
#     pass

@then('The Product Color is Selected')
def verify_user_can_select_colors(context):
    context.driver.find_element(*OPTIONS).click() # click on 1

    all_colors_options = context.driver.find_elements(*OPTIONS) #finds all the color options
    print('All colors:', all_colors_options)
    expected_colors = ['Black', 'Blue, Over Dye', 'Dark Blue Vintage', 'Dark Indigo/Rinsed', 'Dark Khaki Brown',
                       'Dark Wash', 'Indigo Wash', 'Light Blue Vintage', 'Light Khaki Brown', 'Light Wash',
                       'Medium Blue, Vintage', 'Medium Wash', 'Olive', 'Rinsed', 'Sage Green', 'Vintage Wash',
                       'Washed Black', 'Washed Grey']

    color_namelist = []                                         #creating empty list to store colors
    for thumbnail in all_colors_options:
        thumbnail.click()                                       #click on the product thumbnail
        current = context.driver.find_element(*CURRENT).text    #extracting the alt text corresponding to the thumbnail
        print('Current color: ', current)                       #print which color that was just clicked at
        color_namelist += [current]                             #appending to the color name list


    for expected_color in expected_colors:                      #making sure each element is the expected colors list
        assert expected_color in color_namelist, f'Expected {expected_color} not found in list'