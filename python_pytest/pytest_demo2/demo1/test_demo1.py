# -*-coding:utf-8-*-
import pytest


# 读取规则：先读取当前文件里的fixture  ->  当前目录下的conftest  ->  当前项目目录下的conftest
@pytest.fixture()
def connectDB():
    print("testdemo1下的connectDB")


def test_a(connectDB):
    print("demo1- testa")


class TestA:
    def test_b(self):
        print("demo1- testb")
