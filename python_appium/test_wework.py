from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWeWork:
    def setup(self):
        desire_cap = {
            "platformName": "Android",
            "appPackage": "com.tencent.wework",
            "appActivity": "launch.WwMainActivity",
            "noReset": True,
            "deviceName": "127.0.0.1:7555",
            "skipDeviceInitialization": True,
            "settings[waitForIdleTimeout]": 0
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_add_member(self):
        self.driver.find_element_by_xpath('//*[@text = "通讯录"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.driver.find_element_by_id('com.tencent.wework:id/csn').click()
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys('test_9')
        self.driver.find_element_by_xpath("//*[contains(@text,'性别')]/../android.widget.RelativeLayout").click()

        ele = (By.XPATH, "//*[@resource-id='com.tencent.wework:id/elq'and@text='男']")
        # 显示等待，判断元素是否可点击
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ele))
        self.driver.find_element(*ele).click()
        self.driver.find_element_by_xpath("//*[contains(@text,'邮箱')]/../android.widget.EditText").send_keys(
            'test_9@qq.com')
        self.driver.find_element_by_id('com.tencent.wework:id/ie7').click()
        # 获取toast
        ele_toast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        assert '添加成功' == ele_toast
