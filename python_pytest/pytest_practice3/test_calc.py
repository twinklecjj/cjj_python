# -*-coding:utf-8-*-
"""
作业1：
1、编写用例顺序：加- 除-减-乘
2、控制测试用例顺序按照【加-减-乘-除】这个顺序执行
作业2【选做】：
1、注册一个命令行参数env，定义分组hogwarts ,将参数 env放在hogwards分组下
2、env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据
"""
import pytest


# 定义类
class TestCalc:
    # 控制测试用例的执行顺序
    @pytest.mark.run(order=1)
    # 定义一个test_add()方法
    def test_add(self, get_calc, get_adddatas):
        # 调用它的相加add()方法
        result = get_calc.add(get_adddatas[0], get_adddatas[1])
        print(result)
        # 判断result为小数的时候使用round取小数点后两位
        if isinstance(result, float):
            result = round(result, 2)
            return
        # 判断参数中有为str类型的,打印不支持字符串并返回
        elif isinstance(get_adddatas[0], str) or isinstance(get_adddatas[1], str):
            print("不支持字符串")
            return
        # 断言
        assert get_adddatas[2] == result

    # 控制测试用例的执行顺序
    @pytest.mark.run(order=4)
    # 定义一个test_div()方法
    def test_div(self, get_calc, get_divdatas):
        # 调用它的相除div()方法
        result = get_calc.div(get_divdatas[0], get_divdatas[1])
        print(result)
        # 判断除数不能为0
        if get_divdatas[1] == 0:
            print("除数不能为0")
            return
        # 判断输入数据为字符串类型，打印不支持字符串，并返回
        elif isinstance(get_divdatas[0], str) or isinstance(get_divdatas[1], str):
            print("不支持字符串")
            return
        # 断言
        assert get_divdatas[2] == result

    # 控制测试用例的执行顺序
    @pytest.mark.run(order=2)
    # 定义一个test_sub()方法
    def test_sub(self, get_calc, get_subdatas):
        # 调用它的相减sub()方法
        result = get_calc.sub(get_subdatas[0], get_subdatas[1])
        print(result)
        # 判断result为小数的时候使用round取小数点后两位
        if isinstance(result, float):
            result = round(result, 2)
        # 判断输入数据为字符串类型，打印不支持字符串，并返回
        elif isinstance(get_subdatas[0], str) or isinstance(get_subdatas[1], str):
            print("不支持字符串")
            return
        # 断言
        assert get_subdatas[2] == result

    # 控制测试用例的执行顺序
    @pytest.mark.run(order=3)
    # 定义一个test_mul()方法
    def test_mul(self, get_calc, get_muldatas):
        # 调用它的相乘mul()方法
        result = get_calc.mul(get_muldatas[0], get_muldatas[1])
        print(result)
        # 判断result为小数的时候使用round取小数点后两位
        if isinstance(result, float):
            result = round(result, 2)
            # 判断输入数据为字符串类型，打印不支持字符串，并返回
        elif isinstance(get_muldatas[0], str) or isinstance(get_muldatas[1], str):
            print("不支持字符串")
            return
        # 断言
        assert get_muldatas[2] == result
