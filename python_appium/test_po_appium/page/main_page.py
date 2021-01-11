from appium.webdriver.common.mobileby import MobileBy

from python_appium.test_po_appium.page.address_page import AddressPage
from python_appium.test_po_appium.page.base_page import BasePage


class MainPage(BasePage):
    address_element = (MobileBy.XPATH, '//*[@text = "通讯录"]')

    def address_list(self):
        self.find(self.address_element).click()
        # self.find_and_click(self.address_element)
        return AddressPage(self.driver)
