from pages.base_page import BasePage

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    digit_1_selector = (MobileBy.ID, "digit_1")
    digit_2_selector = (MobileBy.ID, "digit_2")
    equals_selector = (MobileBy.ACCESSIBILITY_ID, "equals")
    plus_selector = (MobileBy.ACCESSIBILITY_ID, "plus")
    minus_selector = (MobileBy.ACCESSIBILITY_ID, "minus")
    multiply_selector = (MobileBy.ACCESSIBILITY_ID, "multiply")
    divide_selector = (MobileBy.ACCESSIBILITY_ID, "divide")
    result_selector = (MobileBy.ID, "result_final")

    def add_digits(self):
        self.driver.find_element(*self.digit_1_selector).click()
        self.driver.find_element(*self.plus_selector).click()
        self.driver.find_element(*self.digit_2_selector).click()
        self.driver.find_element(*self.equals_selector).click()

    def get_result(self):
        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.result_selector)).text
        return result
