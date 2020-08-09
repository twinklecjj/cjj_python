# -*-coding:utf-8-*-
# connectDB参数要想全部执行，在第一个方法内至少传递一次（适用于function和module）
# connectDB参数从哪开始传递，从哪开始生效
def test_w(connectDB):
    print("测试用例w")


class TestDemo:
    def test_a(self, connectDB):
        print("测试用例a")

    def test_b(self, connectDB):
        print("测试用例b")


class TestDemo1:
    def test_c(self, connectDB):
        print("测试用例c")

    def test_d(self, connectDB):
        print("测试用例d")
