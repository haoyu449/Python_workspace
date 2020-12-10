import allure
import pytest


@allure.feature('测试计算器')
class TestCalculator:
    @allure.story('测试加法')
    @pytest.mark.run(order=1)
    @pytest.mark.add
    def test_add(self, get_cale, get_add_data):
        result = None
        try:
            result = get_cale.add(get_add_data[0], get_add_data[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_add_data[2]

    @allure.story('测试除法')
    @pytest.mark.run(order=4)
    @pytest.mark.div
    def test_div(self, get_cale, get_div_data):
        result = None
        try:
            result = get_cale.div(get_div_data[0], get_div_data[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_div_data[2]

    @allure.story('测试减法')
    @pytest.mark.run(order=2)
    @pytest.mark.sub
    def test_sub(self, get_cale, get_sub_data):
        result = None
        try:
            result = get_cale.sub(get_sub_data[0], get_sub_data[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)

        assert result == get_sub_data[2]

    @allure.story('测试乘法')
    @pytest.mark.run(order=3)
    @pytest.mark.mul
    def test_mul(self, get_cale, get_mul_data):
        result = None
        try:
            result = get_cale.mul(get_mul_data[0], get_mul_data[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_mul_data[2]
