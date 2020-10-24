from pages.home import HomePage
from pages.contact_us import ContactUsPage


class Tests:

    def setup_method(self, driver):
        self.home_page = HomePage(driver)
        self.contact_us_page = ContactUsPage(driver)

    def test_contact_us(self):
        self.home_page.go_to_contact_us()
        self.contact_us_page.select_subject("1")
        self.contact_us_page.enter_email("seleniumwsh@gmail.com")
        self.contact_us_page.enter_message("test message")
        self.contact_us_page.send_message()
        self.contact_us_page.check_success_message()
    
    
    def test_contact_us_no_email(self):
        self.home_page.go_to_contact_us()
        self.contact_us_page.select_subject("1")
        self.contact_us_page.enter_message("test message")
        self.contact_us_page.send_message()
        self.contact_us_page.check_alert_message()