# -*- coding:utf-8 -*-
"""
复用浏览器
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup(self):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        # 隐式等待,动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(5)
        # 浏览器窗口的最大化
        self.driver.maximize_window()

    def tesrdown(self):
        self.driver.quit()

    def test_demo(self):
        # self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()
        sleep(3)
        category = self.driver.find_element(By.LINK_TEXT, "所有分类")
        assert 'active' == category.get_attribute("class")
