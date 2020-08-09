# -*-coding:utf-8-*-
import pytest
import yaml
import sys

from pytest_demo2.calc import Calculator

sys.path.append('../../..')
print(sys.path)


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


# 读取文件
with open('data/calc.yaml', encoding='utf-8') as f:
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
