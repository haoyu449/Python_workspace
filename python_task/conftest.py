import os
from typing import List

import pytest
import yaml

from python_code.calc import Calculator


@pytest.fixture(scope='class')
def get_cale():
    print('实例化计算器')
    cale = Calculator()
    return cale


# 获取yaml文件所在的绝对路径
yaml_file_path = os.path.dirname(__file__) + '/task_datas.yml'

# yaml文件参数获取
with open(yaml_file_path, encoding='UTF-8') as f:
    datas = yaml.safe_load(f)

    add_datas = datas['add']
    myid_add = datas['myid_add']

    div_datas = datas['div']
    myid_div = datas['myid_div']

    sub_datas = datas['sub']
    myid_sub = datas['myid_sub']

    mul_datas = datas['mul']
    myid_mul = datas['myid_mul']


# 定义加法计算数据
@pytest.fixture(params=add_datas, ids=myid_add)
def get_add_data(request):
    print('开始计算')
    data_add = request.param
    print(f'request.param的数据是:{data_add}')
    yield data_add
    print('结束计算')


# 定义除法计算数据
@pytest.fixture(params=div_datas, ids=myid_div)
def get_div_data(request):
    print('开始计算')
    data_div = request.param
    print(f'request.parm数据是：{data_div}')
    yield data_div
    print('结束计算')


# 定义减法计算数据
@pytest.fixture(params=sub_datas, ids=myid_sub)
def get_sub_data(request):
    print('开始计算')
    data_sub = request.param
    print(f'request.parm的数据是：{data_sub}')
    yield data_sub
    print('结束计算')


# 定义乘法计算数据
@pytest.fixture(params=mul_datas, ids=myid_mul)
def get_mul_data(request):
    print('开始计算')
    data_mul = request.param
    print(f"request.parm的数据是：{data_mul}")
    yield data_mul
    print('结束计算')


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param pytest.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
    print('items')
    print(items)
    # # 实现用例反转
    # items.reverse()
    # 修改测试用例参数编码格式
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
