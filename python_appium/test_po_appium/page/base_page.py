from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_get_text(self, locator):
        return self.find(locator).text

    def find_and_send_keys(self, locator, keys):
        return self.find(locator).send_keys(keys)

    def find_and_scroll(self, text):
        ele = MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().''scrollable(true).instance(0)).' \
                                            'scrollIntoView(new UiSelector().'f'text("{text}").instance(0));'
        return self.find(ele).click()

    def web_driver_wait(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator))
