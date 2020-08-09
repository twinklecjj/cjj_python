# -*-coding:utf-8-*-
"""
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
    使用等价类，边界值，因果图等设计测试用例
    测试用例中添加断言，验证结果
    灵活使用 setup(), teardown() , setup_class(), teardown_class()
"""
# 文件名以test_开头，类名以Test开头，方法名以test_开头
# 注意：测试类里一定不要加__init__()方法
import pytest
import yaml
from python_demo2.pytest_practice1.calc import Calculator
# 读取文件
with open('./calc.yaml',encoding='utf-8') as f:
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


# 定义类
class TestCalc:
    # 定义setup_class()方法
    def setup_class(self):
        print("开始计算")
        # 实例化计算器
        self.calc = Calculator()

    # 定义teardown_class()
    def teardown_class(self):
        print("结束计算")

    def setup(self):
        print("开始测试用例")

    def teardown(self):
        print("结束测试用例")

    # 装饰器
    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect', adddatas, ids=myid)
    # 定义一个test_add()方法
    def test_add(self, a, b, expect):
        # 调用它的相加add()方法
        result = self.calc.add(a, b)
        # 判断result为小数的时候使用round取小数点后两位
        if isinstance(result, float):
            result = round(result, 2)
        elif isinstance(a, str):
            # 断言
            assert expect != result
        elif isinstance(b, str):
            # 断言
            assert expect != result
        # 断言
        assert expect == result

    @pytest.mark.div
    @pytest.mark.parametrize('a,b,expect', adddatas1, ids=myid1)
    # 定义一个test_div()方法
    def test_div(self, a, b, expect):
        # 调用它的相除div()方法
        result = self.calc.div(a, b)
        # 判断除数不能为0
        if b == 0:
            # 断言
            assert expect != result
        # 断言
        assert expect == result
