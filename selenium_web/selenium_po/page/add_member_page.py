from selenium.webdriver.common.by import By

from selenium_web.selenium_po.page.address_list_page import AddressListPage
from selenium_web.selenium_po.page.base_page import BasePage


class AddMemberPage(BasePage):
    ele_name = (By.ID, 'username')
    ele_id = (By.ID, 'memberAdd_acctid')
    ele_number = (By.CSS_SELECTOR, '.ww_telInput_mainNumber')
    ele_save = (By.CSS_SELECTOR, '.js_btn_save')

    def add_member(self, name, id, number):
        self.find(*self.ele_name).send_keys(name)
        self.find(*self.ele_id).send_keys(id)
        self.find(*self.ele_number).send_keys(number)
        self.find(*self.ele_save).click()
        return AddressListPage(self.driver)
