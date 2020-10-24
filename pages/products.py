from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.base import BasePage


class ProductsPage(BasePage):

    product_container_selector = (By.CLASS_NAME, "product-container")
    add_to_cart_selector = (By.CSS_SELECTOR, ".ajax_add_to_cart_button")
    continue_shopping_selector = (By.CSS_SELECTOR, ".continue.button")
    shopping_cart_selector = (By.XPATH, "//*[@class='shopping_cart']/a")

    def add_element_to_cart(self):
        element = self.driver.find_element(*self.product_container_selector)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        self.driver.find_element(*self.add_to_cart_selector).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_shopping_selector)).click()

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.shopping_cart_selector)).click()