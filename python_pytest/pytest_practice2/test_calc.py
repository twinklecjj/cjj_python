# -*-coding:utf-8-*-
"""
1、补全计算器（加减乘除）的测试用例
2、使用fixture方法，完成加减乘除用例的自动生成，添加别名
3、修改测试用例的收集规则，执行所有以 check_开头和test_ 开头的测试用例
4、创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
5、将 Fixture 方法存放在conftest.py ，灵活设置scope的级别
"""


# 定义类
class TestCalc:
    # 定义一个test_add()方法
    def test_add(self, get_calc, get_adddatas):
        # 调用它的相加add()方法
        result = get_calc.add(get_adddatas[0], get_adddatas[1])
        # 判断result为小数的时候使用round取小数点后两位
        if isinstance(result, float):
            result = round(result, 2)
        elif isinstance(get_adddatas[0], str):
            # 断言
            assert get_adddatas[2] != result
        elif isinstance(get_adddatas[1], str):
            # 断言
            assert get_adddatas[2] != result
        # 断言
        assert get_adddatas[2] == result

    def check_sub(self, get_calc, get_subdatas):
        # 调用它的相加add()方法
        result = get_calc.sub(get_subdatas[0], get_subdatas[1])
        # 判断result为小数的时候使用round取小数点后两位
        if isinstance(result, float):
            result = round(result, 2)
        elif isinstance(get_subdatas[0], str):
            # 断言
            assert get_subdatas[2] != result
        elif isinstance(get_subdatas[1], str):
            # 断言
            assert get_subdatas[2] != result
        # 断言
        assert get_subdatas[2] == result

    def test_mul(self, get_calc, get_muldatas):
        # 调用它的相乘mul()方法
        result = get_calc.mul(get_muldatas[0], get_muldatas[1])
        # 判断result为小数的时候使用round取小数点后两位
        if isinstance(result, float):
            result = round(result, 2)
        elif isinstance(get_muldatas[0], str):
            # 断言
            assert get_muldatas[2] != result
        elif isinstance(get_muldatas[1], str):
            # 断言
            assert get_muldatas[2] != result
        # 断言
        assert get_muldatas[2] == result

    # 定义一个check_div()方法
    def check_div(self, get_calc, get_divdatas):
        # 调用它的相除div()方法
        result = get_calc.div(get_divdatas[0], get_divdatas[1])
        # 判断除数不能为0
        if get_divdatas[1] == 0:
            # 断言
            assert get_divdatas[2] != result
        # 断言
        assert get_divdatas[2] == result
