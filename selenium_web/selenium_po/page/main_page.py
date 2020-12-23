from selenium.webdriver.common.by import By

from selenium_web.selenium_po.page.add_member_page import AddMemberPage
from selenium_web.selenium_po.page.address_list_page import AddressListPage
from selenium_web.selenium_po.page.base_page import BasePage


class MainPage(BasePage):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_address_list_page(self):
        self.find(By.ID, 'menu_contacts').click()
        return AddressListPage(self.driver)

    def goto_add_member(self):
        self.find(By.ID, 'menu_index').click()
        self.find(By.CSS_SELECTOR, '.ww_indexImg_AddMember').click()
        return AddMemberPage(self.driver)
