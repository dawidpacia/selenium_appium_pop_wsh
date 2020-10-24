from selenium.webdriver import Chrome


class BasePage:

    def __init__(self, driver: Chrome):
        self.driver = driver
