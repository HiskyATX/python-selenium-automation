from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    # SUBNAV_CATEGORY = (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}']")
    SUBNAV_CATEGORY = (By.XPATH, "//*[@aria-label='{CATEGORY}']")

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)


    def get_subnav_locator(self, category):
        return[self.SUBNAV_CATEGORY[0], self.SUBNAV_CATEGORY[1].replace('{CATEGORY}', category)]


    def verify_selected_dept(self, category):
            locator = self.get_subnav_locator(category)
            self.wait_for_element_appear(*locator)
            # print(locator)
            # self.wait_for_element_appear(*locator)
            # self.find_element()