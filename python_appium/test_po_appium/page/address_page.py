from python_appium.test_po_appium.page.add_member_page import AddMember
from python_appium.test_po_appium.page.base_page import BasePage


class AddressPage(BasePage):
    text = '添加成员'

    def add_member(self):
        self.find_and_scroll(self.text)
        return AddMember(self.driver)
