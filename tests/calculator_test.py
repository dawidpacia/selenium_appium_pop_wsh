import os
from appium import webdriver
from pages.home_page import HomePage
from time import sleep

app_name = "calculator.apk"
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = app_path

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
home_page = HomePage(driver)


def test_log():
    home_page.wait_until_panel_is_hidden()
    home_page.calculate_log()
    result = home_page.get_result()
    assert result == "1"


def test_add():
    home_page.add_digits(1, 2)
    result = home_page.get_result()
    assert result == "3"


def test_sub():
    home_page.sub_digits(1, 2)
    result = home_page.get_result()
    assert result == "−1"


def test_mul():
    home_page.mul_digits(1, 2)
    result = home_page.get_result()
    assert result == "2"


def test_div():
    home_page.div_digits(1, 2)
    result = home_page.get_result()
    assert result == "0.5"
