# -*- coding:utf-8 -*-
from time import sleep

import pytest


# 控制执行顺序
# 方法二
@pytest.mark.forth
# # 方法一
# @pytest.mark.run(order=3)
def test_foo():
    sleep(1)
    assert True


# 方法二
@pytest.mark.third
# # 方法一
# @pytest.mark.run(order=2)
def test_bar():
    sleep(1)
    assert True


# 方法二
@pytest.mark.second
# # 方法一
# @pytest.mark.run(order=1)
def test_aar():
    sleep(1)
    assert True
