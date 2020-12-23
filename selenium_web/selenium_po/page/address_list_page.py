from time import sleep

from selenium.webdriver.common.by import By

from selenium_web.selenium_po.page.base_page import BasePage


class AddressListPage(BasePage):

    def click_add_member(self):
        from selenium_web.selenium_po.page.add_member_page import AddMemberPage
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        self.wait_for_click(ele, 5)
        while True:
            self.find(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
            element = self.finds(By.ID, "username")
            if len(element) > 0:
                break
        return AddMemberPage(self.driver)

    def get_member(self):
        sleep(1)
        ele_member = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        name_list = []
        for value in ele_member:
            print(value.get_attribute('title'))
            name_list.append(value.get_attribute('title'))
        return name_list
