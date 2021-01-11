import pytest
import yaml

from python_appium.test_po_appium.page.app import App


class TestPo:
    def setup(self):
        self.app = App()
        self.main = self.app.start_app().goto_main()

    def teardown(self):
        self.app.stop_app()

    # @pytest.mark.parametrize('name, gender, mail', [('test_11', '女', 'test_11@qq.com')])
    @pytest.mark.parametrize('name, gender, mail', yaml.safe_load(open('data.yaml', encoding='utf-8'))['add'])
    def test_add_member(self, name, gender, mail):
        toast_ele = self.main.address_list().add_member().manual_input(). \
            member_name(name).member_gender(gender).member_mail(mail).member_save().get_toast()
        assert '添加成功' == toast_ele
