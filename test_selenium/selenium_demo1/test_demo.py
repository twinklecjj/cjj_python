# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo():
    def setup(self):
        # 没有配置环境变量
        # self.driver=webdriver.firefox(executable_path="F:/driver/geckodriver")
        self.driver = webdriver.Chrome()
        # 隐式等待,动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(5)
        # 浏览器窗口的最大化
        self.driver.maximize_window()

    def tesrdown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()
        sleep(3)
        category = self.driver.find_element(By.LINK_TEXT, "所有分类")
        assert 'active' == category.get_attribute("class")
