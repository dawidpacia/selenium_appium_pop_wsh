import pytest
from selenium_tests import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium_tests.pages import ContactUsPage
from selenium_tests.pages import HomePage


@pytest.fixture()
def driver(request):

    def close_driver():
        wd.quit()

    BASE_URL = "http://automationpractice.com/"

    wd = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    wd.get(BASE_URL)

    request.addfinalizer(close_driver)
    home_page = HomePage(wd)
    contact_us_page = ContactUsPage(wd)

    return wd

