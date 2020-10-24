from pages.home import HomePage
from pages.contact_us import ContactUsPage


def test_contact_us(driver):
    home_page = HomePage(driver)
    contact_us_page = ContactUsPage(driver)

    home_page.go_to_contact_us()
    contact_us_page.select_subject("1")
    contact_us_page.enter_email("seleniumwsh@gmail.com")
    contact_us_page.enter_message("test message")
    contact_us_page.send_message()
    contact_us_page.check_success_message()


def test_contact_us_no_email(driver):
    home_page = HomePage(driver)
    contact_us_page = ContactUsPage(driver)

    home_page.go_to_contact_us()
    contact_us_page.select_subject("1")
    contact_us_page.enter_message("test message")
    contact_us_page.send_message()
    contact_us_page.check_alert_message()