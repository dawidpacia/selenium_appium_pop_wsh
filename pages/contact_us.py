from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from pages.base import BasePage


class ContactUsPage(BasePage):

    subject_selector = (By.XPATH, "//*[@id='id_contact']")
    email_selector = (By.ID, "email")
    message_selector = (By.ID, "message")
    submit_button_selector = (By.ID, "submitMessage")
    success_email_sent_selector = (By.CSS_SELECTOR, ".alert-success")
    alert_message_selector = (By.CSS_SELECTOR, ".alert-danger")

    def select_subject(self, number):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.subject_selector))
        select = Select(element)
        select.select_by_value(number)

    def enter_email(self, email):
        self.driver.find_element(*self.email_selector).send_keys(email)

    def enter_message(self, message):
        self.driver.find_element(*self.message_selector).send_keys(message)

    def send_message(self):
        self.driver.find_element(*self.submit_button_selector).click()

    def check_success_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.success_email_sent_selector))

    def check_alert_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.message_selector))
