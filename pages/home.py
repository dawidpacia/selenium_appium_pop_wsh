from selenium.webdriver.common.by import By

from pages.base import BasePage


class HomePage(BasePage):

    contact_us_selector = (By.ID, "contact-link")

    def go_to_contact_us(self):
        self.driver.find_element(*self.contact_us_selector).click()
