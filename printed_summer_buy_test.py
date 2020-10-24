from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_printed_summer_buy(driver):
    search_box_selector = (By.ID, "search_query_top")
    submit_search_selector = (By.NAME, "submit_search")
    product_container_selector = (By.CLASS_NAME, "product-container")
    add_to_cart_selector = (By.CSS_SELECTOR, ".ajax_add_to_cart_button")
    checkout_button_selector = (By.XPATH, "//a[@title='Proceed to checkout']")
    product_description_selector = (By.CSS_SELECTOR, ".cart_description > .product-name  > a")


    driver.find_element(*search_box_selector).send_keys("Printed Summer")
    driver.find_element(*submit_search_selector).click()

    element = driver.find_element(*product_container_selector)

    hover = ActionChains(driver).move_to_element(element)
    hover.perform()
    driver.find_element(*add_to_cart_selector).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(checkout_button_selector)).click()
    product_description_element = driver.find_element(*product_description_selector).text

    assert "Printed Summer" in product_description_element

