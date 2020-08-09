# -*-coding:utf-8-*-
import pytest


# 定义类
class TestCalc:
    # # 定义setup_class()方法
    # def setup_class(self):
    #     print("开始计算")
    #     # 实例化计算器
    #     self.calc = Calculator()
    #
    # # 定义teardown_class()
    # def teardown_class(self):
    #     print("结束计算")
    #
    # def setup(self):
    #     print("开始测试用例")
    #
    # def teardown(self):
    #     print("结束测试用例")

    # 装饰器
    @pytest.mark.add
    # 定义一个test_add()方法
    def test_add(self, get_calc, get_datas):
        # 调用它的相加add()方法
        result = get_calc.add(get_datas[0], get_datas[1])
        # 判断result为小数的时候使用round取小数点后两位
        if isinstance(result, float):
            result = round(result, 2)
        elif isinstance(get_datas[0], str):
            # 断言
            assert get_datas[2] != result
        elif isinstance(get_datas[1], str):
            # 断言
            assert get_datas[2] != result
        # 断言
        assert get_datas[2] == result

    @pytest.mark.div
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
