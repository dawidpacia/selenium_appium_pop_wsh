from selenium_tests import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium_tests.webdriver.common.by import By
from selenium_tests.webdriver.common.action_chains import ActionChains
from selenium_tests.webdriver.support.wait import WebDriverWait
from selenium_tests.webdriver.support import expected_conditions as EC
from selenium_tests.webdriver.support.ui import Select


def test_contact_us(driver):

    contact_us_selector = (By.ID, "contact-link")
    subject_selector = (By.XPATH, "//*[@id='id_contact']")
    email_selector = (By.ID, "email")
    message_selector = (By.ID, "message")
    submit_button_selector = (By.ID, "submitMessage")
    alert_email_sent_selector = (By.CSS_SELECTOR, ".alert-success")


    driver.find_element(*contact_us_selector).click()

    #driver.find_element(*subject_selector).click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(subject_selector))
    select = Select(element)
    select.select_by_value("1")

    driver.find_element(*email_selector).send_keys("seleniumwsh@gmail.com")
    driver.find_element(*message_selector).send_keys("test message")
    driver.find_element(*submit_button_selector).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(alert_email_sent_selector))
