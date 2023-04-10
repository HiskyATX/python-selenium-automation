from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    RETURNS_AND_ORDERS = (By.CSS_SELECTOR, '#nav-orders')
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    NEW_ARRIVALS = (By.XPATH, "//*[@aria-label='New Arrivals']")
    FLOATING_MENU = (By.XPATH, "//*[@id='nav-flyout-aj:https://m.media-amazon.com/images/G/01/Softlines/Store/MegaMenu/megamenucreator_removeps_en_US.json:subnav-sl-megamenu-8:0']")

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)


    def click_search(self):
        self.click(*self.SEARCH_ICON)
        #self.wait_for_element_click(*self.SEARCH_ICON)


    def click_returns_and_orders(self):
        self.click(*self.RETURNS_AND_ORDERS)


    def select_department(self, alias):
        department_dd = self.find_element(*self.DEPARTMENT_SELECTION)
        selects = Select(department_dd)
        selects.select_by_value(f'search-alias={alias}')


    def hover_over_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()


    def verify_categories_appear(self):
        # assigning a variable to the return of a valid object, if it appears
        obj = self.wait_for_element_appear(*self.FLOATING_MENU)

        return obj


