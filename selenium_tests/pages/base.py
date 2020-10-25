from selenium_tests.webdriver import Chrome


class BasePage:

    def __init__(self, driver: Chrome):
        self.driver = driver
