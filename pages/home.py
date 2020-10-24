from selenium.webdriver.common.by import By

from pages.base import BasePage


class HomePage(BasePage):

    contact_us_selector = (By.ID, "contact-link")
    search_box_selector = (By.ID, "search_query_top")
    submit_search_selector = (By.NAME, "submit_search")

    def go_to_contact_us(self):
        self.driver.find_element(*self.contact_us_selector).click()

    def search_product(self, product_name):
        self.driver.find_element(*self.search_box_selector).clear()
        self.driver.find_element(*self.search_box_selector).send_keys(product_name)
        self.driver.find_element(*self.submit_search_selector).click()