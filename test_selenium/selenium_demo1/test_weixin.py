# -*- coding:utf-8 -*-
"""
使用cookie
"""
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup(self):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        # 隐式等待,动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(5)
        # 浏览器窗口的最大化
        self.driver.maximize_window()

    def tesrdown(self):
        self.driver.quit()

    def test_cookie(self):
        # get_cookies()获取当前页面的cookies
        # cookies=self.driver.get_cookies()
        # print(cookies)
        # 打开index页面，这时候需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 带有登录信息的cookie
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850902138378'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'Oqg_txmY9UhP043trqhH8CKLmzV9gCrWyAqBMv9A0bI7jFWVq7zUoTPrB8Vm0C_RmDtCBzhkXRDjFNhLaZE9MT5WTwCiv24oFrYok5I0FKpAao9uwJ4fSW0wW8PW55g5twvUeyYy7NRd725CTHpOawmgyso9hXfNo24GN5HTBS_UyQWKEbIafqqw1R1_eaFivGGBKTt77bnOzb2C3W1rgmdtlMg33w6O2JSkVo6omcTtlw4weICeP0nHtuKPN1hgIu6E8tYoTeQUuEkJ-O6Rug'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850902138378'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325041161398'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a1951958'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1597991088, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '6m3h98j'},
            {'domain': '.qq.com', 'expiry': 1598047301, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.969595823.1597960300'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1597960132'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '02351591'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'aBK9UEQb0bfmyROkcdj4yb_0JZSnfhbQwOaNMuItqFUShgs4CzWAwoGgLUS8QRIt'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629496131, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1597960132'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1661032901, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.82080879.1597669954'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629205932, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600553547, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # 重新打开已带有cookie信息的index页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def test_importcontacts(self):
        # 打开index页面，这时候需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 带有登录信息的cookie
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850902138378'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'Oqg_txmY9UhP043trqhH8CKLmzV9gCrWyAqBMv9A0bI7jFWVq7zUoTPrB8Vm0C_RmDtCBzhkXRDjFNhLaZE9MT5WTwCiv24oFrYok5I0FKpAao9uwJ4fSW0wW8PW55g5twvUeyYy7NRd725CTHpOawmgyso9hXfNo24GN5HTBS_UyQWKEbIafqqw1R1_eaFivGGBKTt77bnOzb2C3W1rgmdtlMg33w6O2JSkVo6omcTtlw4weICeP0nHtuKPN1hgIu6E8tYoTeQUuEkJ-O6Rug'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850902138378'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325041161398'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a1951958'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1597991088, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '6m3h98j'},
            {'domain': '.qq.com', 'expiry': 1598047301, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.969595823.1597960300'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1597960132'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '02351591'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'aBK9UEQb0bfmyROkcdj4yb_0JZSnfhbQwOaNMuItqFUShgs4CzWAwoGgLUS8QRIt'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629496131, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1597960132'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1661032901, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.82080879.1597669954'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629205932, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600553547, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'}]

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # 重新打开已带有cookie信息的index页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 定位到导入通讯录，并点击
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 定位到“上传文件”按钮，并上传文件
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys(
            r"C:/Users\Administrator/Desktop/实战/18 Web自动化测试/01 企业微信的自动化登录（一）（二）/mydata.xlsx")
        # 断言测试结果的准确性，判断上传成功的文件名是否正确
        assert "mydata.xlsx" == self.driver.find_element(By.ID, "upload_file_name").text
        sleep(3)

    # 实现cookie数据的持久化存储
    def test_shelve(self):
        # shelve python内置的模块，相当于小型的数据库
        db = shelve.open('./mydbs/cookies')
        # db['cookie']=cookies
        # db.close()
        cookies = db['cookie']
        # 打开index页面，这时候需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # 重新打开已带有cookie信息的index页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 定位到导入通讯录，并点击
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 定位到“上传文件”按钮，并上传文件
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys(
            r"C:/Users\Administrator/Desktop/实战/18 Web自动化测试/01 企业微信的自动化登录（一）（二）/mydata.xlsx")
        # 断言测试结果的准确性，判断上传成功的文件名是否正确
        assert "mydata.xlsx" == self.driver.find_element(By.ID, "upload_file_name").text
        sleep(3)
