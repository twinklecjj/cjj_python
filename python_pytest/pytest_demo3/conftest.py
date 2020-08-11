# -*-coding:utf-8-*-
from typing import List

import pytest
import yaml
import sys

from pytest_demo3.calc import Calculator

sys.path.append('../../..')
print(sys.path)

import os


# 作用域：session>module>class>function
# function：方法或函数级别调用一次
# @pytest.fixture(scope='function')
# class：类级别调用一次
# @pytest.fixture(scope='class')
# module：模块级别调用一次
# @pytest.fixture(scope='module')
# session:多个文件只调用一次
@pytest.fixture(scope='session')
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库连接")


@pytest.fixture(scope='class')
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc


# 通过os.path.dirname(__file__)能够获取当前文件所在的目录
yamlfilepath = os.path.dirname(__file__) + "/data/calc.yaml"
# ./data/calc.yaml  ====>.代表当前路径，也就是说你在哪个路径下执行测试文件，就叫做当前路径
# 读取文件
with open(yamlfilepath, encoding='utf-8') as f:
    # safe_load()只能一次
    data = yaml.safe_load(f)
    # 获取add下的datas里的数据
    adddatas = data['add']['datas']
    print(adddatas)
    # 获取add下的myid里的数据
    myid = data['add']['myid']
    print(myid)
    # 获取div下的datas里的数据
    adddatas1 = data['div']['datas']
    print(adddatas1)
    # 获取div下的myid里的数据
    myid1 = data['div']['myid']
    print(myid1)


@pytest.fixture(params=adddatas, ids=myid)
def get_datas(request):
    data = request.param
    print(f"request.param的测试数据是：{data}")
    return data


# 如果不去定义这些hook函数，它会按照pytest默认的规则去运行测试用例
# 如果在conftest.py文件里面定义的这些hook函数，名字和参数要与官网定义的一模一样
# 在hook函数内部实现要改写的规则
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
    # 测试用例反转
    items.reverse()
    # 测试用例参数的编码格式改写
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        # 如果测试用例里面有字符，则自动的添加一些标签
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
        if 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)


# parser：用户命令行参数与ini文件值得解析器
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")  # group将下面所有的option都展示在这个group下
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 默认值
                      dest='env',  # 存储的变量
                      help='set your run env'  # 参数说明
                      )
    mygroup.addoption("--des",  # 注册一个命令行选项
                      default='cjj',  # 默认值
                      dest='cjj',  # 存储的变量
                      help='set your param'  # 参数说明
                      )


# 获取参数
@pytest.fixture(scope='session')
def cmdoption(request):
    return request.config.getoption("--env", default='test')
