# -*-coding:utf-8-*-
import pytest
import yaml
import sys

sys.path.append('../../..')
print(sys.path)
from pytest_practice2.calc import Calculator


@pytest.fixture(scope='function')
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")


# 读取文件
with open('./calc.yaml', encoding='utf-8') as f:
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


@pytest.fixture(params=adddatas, ids=myid1)
def get_adddatas(request):
    data = request.param
    print(f"加法的测试数据是：{data}")
    return data


@pytest.fixture(params=subdatas, ids=myid2)
def get_subdatas(request):
    data = request.param
    print(f"减法的测试数据是：{data}")
    return data


@pytest.fixture(params=muldatas, ids=myid3)
def get_muldatas(request):
    data = request.param
    print(f"乘法的测试数据是：{data}")
    return data


@pytest.fixture(params=divdatas, ids=myid4)
def get_divdatas(request):
    data = request.param
    print(f"除法的测试数据是：{data}")
    return data
