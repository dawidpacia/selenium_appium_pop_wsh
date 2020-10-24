import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.contact_us import ContactUsPage
from pages.home import HomePage


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

