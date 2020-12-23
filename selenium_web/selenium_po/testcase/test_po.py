import allure
import pytest
import yaml

from selenium_web.selenium_po.page.main_page import MainPage


class TestPo:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.skip
    @allure.title('通讯录点击添加成员')
    @pytest.mark.parametrize('name, id, number', [('test_5', 'test_5', '12345678914')])
    def test_login(self, name, id, number):
        # name = 'test_4'
        # id = 'test_4'
        # number = 12345678913
        name_list = self.main.goto_address_list_page().click_add_member().add_member(name, id, number).get_member()
        print(name_list)
        assert name in name_list

    @allure.title('首页点击添加成员')
    @pytest.mark.parametrize('name, id, number', yaml.safe_load(open('./data.yaml', encoding="utf-8")))
    def test_main_login(self, name, id, number):
        name_list = self.main.goto_add_member().add_member(name, id, number).get_member()
        print(name_list)
        assert name in name_list
