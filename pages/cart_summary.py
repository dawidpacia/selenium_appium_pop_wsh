from selenium.webdriver.common.by import By

from pages.base import BasePage


class CartSummaryPage(BasePage):
    product_description_selector = (By.CSS_SELECTOR, ".cart_description > .product-name  > a")

    def get_all_elements(self):
        products_elements = self.driver.find_elements(*self.product_description_selector)
        products_name = ""
        for product in products_elements:
            products_name += product.text
        return products_name
