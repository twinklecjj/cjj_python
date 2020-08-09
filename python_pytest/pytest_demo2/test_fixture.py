# -*-coding:utf-8-*-
import pytest


# 创建一个登录的fixture方法,yield关键字激活了fixture的teardown方法
# fixture是pytest的外壳函数，可以模拟setup、teardown操作
# yield之前的操作相当于setup，yield之后的操作相当于teardown
# yield相当于return，如果想要return一些测试数据，可以放在yield后面返回到测试用例中
# autouse=True：所有测试用例都自动实现自动应用
@pytest.fixture(autouse=True)
def login():
    print("登录操作")
    print("获取token")
    username = "tom"
    password = "123456"
    # 使用return，没有teardown操作
    # return [username,password]
    yield [username, password]
    print("登出操作")


# 测试用例1：需要提前登录
# 在执行测试用例之前会执行传入的fixture方法
def test_case1(connectDB):
    # 想要fixture提供的返回数据，直接在方法体内使用fixture名字，就可以调用return回来的数据
    print(f"login username and password:{login}")
    print("测试用例1")


# 测试用例2：不需要提前登录
def test_case2():
    print("测试用例2")


# 测试用例3：需要提前登录
def test_case3():
    print("测试用例3")


# 测试用例4：需要提前登录
def test_case4():
    print("测试用例4")
