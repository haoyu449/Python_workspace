from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, base_url=None):
        print(base_url)
        if base_url is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
        else:
            self.driver = base_url

    # 封装find
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # 封装finds
    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    # 封装显示等待
    def wait_for_click(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
