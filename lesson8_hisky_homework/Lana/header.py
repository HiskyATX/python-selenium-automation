from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    RETURNS_AND_ORDERS = (By.CSS_SELECTOR, '#nav-orders')
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    #DEPARTMENT_SELECTION = (By.CSS_SELECTOR, '.nav-search-dropdown.searchSelect.nav-progressive-attrubute.nav-progressive-search-dropdown')


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

