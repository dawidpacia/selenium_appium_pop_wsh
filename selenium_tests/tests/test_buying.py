from selenium_tests.pages import HomePage
from selenium_tests.pages.products import ProductsPage
from selenium_tests.pages.cart_summary import CartSummaryPage


def test_buy_different_products(driver):
    home_page = HomePage(driver)
    products_page = ProductsPage(driver)
    cart_summary_page = CartSummaryPage(driver)

    home_page.search_product("Chiffon")
    products_page.add_element_to_cart()
    home_page.search_product("Blouse")
    products_page.add_element_to_cart()
    products_page.proceed_to_checkout()
    products = cart_summary_page.get_all_elements()
    assert "Chiffon" in products
    assert "Blouse" in products
