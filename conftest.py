import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture()
def driver(request):

    def close_driver():
        wd.quit()

    BASE_URL = "http://automationpractice.com/"

    wd = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    wd.get(BASE_URL)

    request.addfinalizer(close_driver)
    return wd

