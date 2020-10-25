import os
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage

app_name = "calculator.apk"
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = app_path

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
home_page = HomePage(driver)


def test_add():
    home_page.add_digits()
    result = home_page.get_result()
    assert result == "3"


# def test_sub():
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((MobileBy.ID, "digit_1"))).click()
#     driver.find_element_by_accessibility_id("minus").click()
#     driver.find_element_by_id("digit_2").click()
#     driver.find_element_by_accessibility_id("equals").click()
#     result = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.ID, "result_final"))).text
#     assert result == "−1"
#
#
# def test_mul():
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((MobileBy.ID, "digit_1"))).click()
#     driver.find_element_by_accessibility_id("multiply").click()
#     driver.find_element_by_id("digit_2").click()
#     driver.find_element_by_accessibility_id("equals").click()
#     result = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.ID, "result_final"))).text
#     assert result == "2"
#
#
# def test_div():
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((MobileBy.ID, "digit_1"))).click()
#     driver.find_element_by_accessibility_id("divide").click()
#     driver.find_element_by_id("digit_2").click()
#     driver.find_element_by_accessibility_id("equals").click()
#     result = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.ID, "result_final"))).text
#     assert result == "0.5"
