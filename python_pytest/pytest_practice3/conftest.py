# -*-coding:utf-8-*-
from typing import List

import pytest
import yaml
import sys

sys.path.append('../../..')
print(sys.path)
from pytest_practice3.calc import Calculator
import os


@pytest.fixture(scope='function')
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")


# 读取文件
yamlfilepath = os.path.dirname(__file__) + "/data/calc.yaml"
with open(yamlfilepath, encoding='utf-8') as f:
    # safe_load()只能一次
    data = yaml.safe_load(f)
    # 获取add下的datas里的数据
    adddatas = data['add']['datas']
    print(adddatas)
    # 获取add下的myid里的数据
    myid1 = data['add']['myid']
    print(myid1)
    # 获取sub下的datas里的数据
    subdatas = data['sub']['datas']
    print(subdatas)
    # 获取sub下的myid里的数据
    myid2 = data['sub']['myid']
    print(myid2)
    # 获取mul下的datas里的数据
    muldatas = data['mul']['datas']
    print(muldatas)
    # 获取mul下的myid里的数据
    myid3 = data['mul']['myid']
    print(myid3)
    # 获取div下的datas里的数据
    divdatas = data['div']['datas']
    print(divdatas)
    # 获取div下的myid里的数据
    myid4 = data['div']['myid']
    print(myid4)


# 使用fixture生成add的别名
@pytest.fixture(params=adddatas, ids=myid1)
def get_adddatas(request):
    data = request.param
    print(f"加法的测试数据是：{data}")
    return data


# 使用fixture生成sub的别名
@pytest.fixture(params=subdatas, ids=myid2)
def get_subdatas(request):
    data = request.param
    print(f"减法的测试数据是：{data}")
    return data


# 使用fixture生成mul的别名
@pytest.fixture(params=muldatas, ids=myid3)
def get_muldatas(request):
    data = request.param
    print(f"乘法的测试数据是：{data}")
    return data


# 使用fixture生成div的别名
@pytest.fixture(params=divdatas, ids=myid4)
def get_divdatas(request):
    data = request.param
    print(f"除法的测试数据是：{data}")
    return data


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param _pytest.main.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[_pytest.nodes.Item] items: List of item objects.
    """
    print("items")
    print(items)
    # 测试用例参数的编码格式改写
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# parser：用户命令行参数与ini文件值得解析器
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")  # group将下面所有的option都展示在这个group下
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 默认值
                      dest='env',  # 存储的变量
                      help='测试环境'  # 参数说明
                      )
    mygroup.addoption("--dev",  # 注册一个命令行选项
                      default='dev',  # 默认值
                      dest='dev',  # 存储的变量
                      help='dev测试环境'  # 参数说明
                      )
    mygroup.addoption("--st",  # 注册一个命令行选项
                      default='st',  # 默认值
                      dest='st',  # 存储的变量
                      help='st测试环境'  # 参数说明
                      )


# 获取参数
@pytest.fixture(scope='session')
def cmdoption(request):
    return request.config.getoption("--env", default='test')


@pytest.fixture(scope='session')
def cmdoption1(request):
    return request.config.getoption("--dev", default='dev')


@pytest.fixture(scope='session')
def cmdoption2(request):
    return request.config.getoption("--st", default='st')
