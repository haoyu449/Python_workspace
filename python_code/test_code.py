import pytest
import yaml

from python_code.calc import Calculator


class TestCalculator:
    def setup_class(self):
        print('开始计算')
        # 实例化变量
        self.cale = Calculator()

    def teardown_class(self):
        print('计算结束')

    @pytest.mark.parametrize(
        'a, b, expect', yaml.safe_load(open('datas.yml'))['add'], ids=yaml.safe_load(open('datas.yml'))['myid_add']
    )
    def test_add(self, a, b, expect):
        result = self.cale.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open('datas.yml'))['div'],
                             ids=yaml.safe_load(open('datas.yml'))['myid_div'])
    def test_div(self, a, b, expect):
        if b != 0:
            result = self.cale.div(a, b)
            if isinstance(result, float):
                result = round(result, 2)
                assert result == expect
        else:
            print('分母不能为0')

# def test():
#     with open('datas.yml', encoding='UTF-8') as f:
#         demo = yaml.safe_load(f)
#         print(demo)
