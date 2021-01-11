from appium.webdriver.common.mobileby import MobileBy

from python_appium.test_po_appium.page.base_page import BasePage
from python_appium.test_po_appium.page.member_information_page import MemberInformation


class AddMember(BasePage):
    manual_element = (MobileBy.ID, 'com.tencent.wework:id/csn')
    toast_element = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def manual_input(self):
        self.find_and_click(self.manual_element)
        return MemberInformation(self.driver)

    def get_toast(self):
        toast = self.find_and_get_text(self.toast_element)
        return toast
