"""
启动APP，关闭APP，重启app
"""
from appium import webdriver

from python_appium.test_po_appium.page.base_page import BasePage
from python_appium.test_po_appium.page.main_page import MainPage


class App(BasePage):
    def start_app(self):
        if self.driver is None:
            desire_cap = {
                "platformName": "Android",
                "appPackage": "com.tencent.wework",
                "appActivity": "launch.WwMainActivity",
                "noReset": 'true',
                "deviceName": "127.0.0.1:7555",
                "skipDeviceInitialization": 'true',
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_cap)
            self.driver.implicitly_wait(10)

        # 获取desire_cap信息,启动APP
        else:
            self.driver.launch_app()
        return self

    def stop_app(self):
        self.driver.quit()

    def reset_app(self):
        self.driver.close()
        self.driver.launch_app()

    def goto_main(self):
        return MainPage(self.driver)
