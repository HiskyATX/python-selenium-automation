from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from pages.header import Page

class SignIn(Page):
    SIGN_IN_VERIFICATION = (By.XPATH, "//h1[contains(text(), 'Sign in')]")

    def verify_sign_in_opens(self):
        assert self.find_element(*self.SIGN_IN_VERIFICATION)  != None
 #       self.driver.wait.until(EC.visibility_of_element_located(*self.SIGN_IN_VERIFICATION))


        # def verify_signin_popup_not_visible(context):
        #     context.driver.wait.until_not(
        #         EC.visibility_of_element_located(SIGN_IN_BTN),
        #         message='Signin btn did not disappear'

        # def click_signin(context):
        #     context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN)).click()
        #     # Feel free to add error message if needed too, for example:
        #     context.driver.wait.until(
        #         EC.element_to_be_clickable(SIGN_IN_BTN),
        #         message='Sign in btn not clickable'
        #     ).click()
        #     )