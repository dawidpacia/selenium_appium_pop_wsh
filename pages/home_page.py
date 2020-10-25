from appium.webdriver.common.touch_action import TouchAction

from pages.base_page import BasePage


from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    equals_selector = (MobileBy.ACCESSIBILITY_ID, "equals")
    plus_selector = (MobileBy.ACCESSIBILITY_ID, "plus")
    minus_selector = (MobileBy.ACCESSIBILITY_ID, "minus")
    multiply_selector = (MobileBy.ACCESSIBILITY_ID, "multiply")
    divide_selector = (MobileBy.ACCESSIBILITY_ID, "divide")
    result_selector = (MobileBy.ID, "result_final")

    def add_digits(self, val_1, val_2):
        self.driver.find_element(*self.digit_locator(val_1)).click()
        self.driver.find_element(*self.plus_selector).click()
        self.driver.find_element(*self.digit_locator(val_2)).click()
        self.driver.find_element(*self.equals_selector).click()

    def sub_digits(self, val_1, val_2):
        self.driver.find_element(*self.digit_locator(val_1)).click()
        self.driver.find_element(*self.minus_selector).click()
        self.driver.find_element(*self.digit_locator(val_2)).click()
        self.driver.find_element(*self.equals_selector).click()

    def div_digits(self, val_1, val_2):
        self.driver.find_element(*self.digit_locator(val_1)).click()
        self.driver.find_element(*self.divide_selector).click()
        self.driver.find_element(*self.digit_locator(val_2)).click()
        self.driver.find_element(*self.equals_selector).click()

    def mul_digits(self, val_1, val_2):
        self.driver.find_element(*self.digit_locator(val_1)).click()
        self.driver.find_element(*self.multiply_selector).click()
        self.driver.find_element(*self.digit_locator(val_2)).click()
        self.driver.find_element(*self.equals_selector).click()

    def get_result(self):
        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.result_selector)).text
        return result

    def digit_locator(self, value):
        selector = (MobileBy.ID, f"digit_{value}")
        return selector

    def open_expert_panel(self):
        TouchAction(self.driver).tap(None, 1000, 1500).perform()
