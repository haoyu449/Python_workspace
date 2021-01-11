from appium.webdriver.common.mobileby import MobileBy

from python_appium.test_po_appium.page.base_page import BasePage


class MemberInformation(BasePage):
    name_element = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
    gender_element = (MobileBy.XPATH, "//*[contains(@text,'性别')]/../android.widget.RelativeLayout")
    man_element = (MobileBy.XPATH, "//*[@text='男']")
    women_element = (MobileBy.XPATH, "//*[@text='女']")
    mail_element = (MobileBy.XPATH, "//*[contains(@text,'邮箱')]/../android.widget.EditText")
    save_element = (MobileBy.ID, 'com.tencent.wework:id/ie7')

    def member_name(self, name):
        self.find_and_send_keys(self.name_element, name)
        return self

    def member_gender(self, gender):
        self.find_and_click(self.gender_element)
        # 显示等待元素可点击
        self.web_driver_wait(self.man_element, 10)
        if gender == '女':
            self.find_and_click(self.women_element)
        else:
            self.find_and_click(self.man_element)
        return self

    def member_mail(self, mail):
        self.find_and_send_keys(self.mail_element, mail)
        return self

    def member_save(self):
        from python_appium.test_po_appium.page.add_member_page import AddMember
        self.find_and_click(self.save_element)
        return AddMember(self.driver)
