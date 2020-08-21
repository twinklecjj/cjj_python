# -*- coding:utf-8 -*-
"""
使用cookie登录企业微信，完成导入联系人，加上断言验证
"""
import os
import shelve
from datetime import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestCookie():
    def setup(self):
        # 复用浏览器
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        # # 实例化driver
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)
        # 浏览器窗口最大化
        self.driver.maximize_window()

    def tesrdown(self):
        # 资源回收driver
        self.driver.quit()

    def test_cookie(self):
        # get_cookies()获取当前页面的cookies
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # 带有登录信息的cookie
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688850902138378'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': '6gVJ8l_aBzkB-FQhMylDyHpvglPV3pmHPQsCoUOro-f2Eb0JeQ7XWxnRJEE2YqjA0nonJr_Av2MrUZhL9qTLPMRgbi5YfjYJNN67Hgjayky_VE7jeOnkH-4xuRL2sAm4VKa67FCdc7kBeBE0wC7zBtKyRezkbmtwFDrDBbO8-BM2nrTPSouD2Jy9et6n9uoWgHYxee4tRi49d9PmcH6mmjecQMvOfNvbOaU0UUzr8kwsIZxQeXhE1EhyQeGsNroXQF_Mh2V8ZMx_3VxOdfynBA'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688850902138378'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970325041161398'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a672640'},
        #     {'domain': '.qq.com', 'expiry': 1598108997, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.969595823.1597960300'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1598054102, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '66fp925'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '0566177'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'aBK9UEQb0bfmyROkcdj4yaq1MyKQjQsmcDtHXqkvw7tycOlXVvtATYWTe6QfR91n'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629496131, 'httpOnly': False,
        #                      'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
        #                      'value': '1597960132'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.qq.com', 'expiry': 1598022637, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.qq.com', 'expiry': 1661094597, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.82080879.1597669954'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1629205932, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1600614598, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh-cn'}]
        # shelve python内置的模块，相当于小型的数据库
        # 存cookies
        db = shelve.open('./mydbs/cookies')
        # db['cookie']=cookies
        # db.close()
        # 取cookie
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
        # 文件名正确，定位到“确认导入”按钮，并点击
        self.driver.find_element(By.ID, "submit_csv").click()
        # 强制等待3秒
        sleep(3)

    def is_login_cookies_work(driver: webdriver) -> bool:
        """通过保存在文件中的cookies中的过期时间判断cookies是否还有效"""
        if not os.path.exists('cookies.dat'):
            return False
        file = shelve.open('./mydbs/cookies')
        cookies = file['cookies']
        file.close()
        if len(cookies) == 0:
            return False
        for cookie in cookies:
            if cookie.get('name') in ['_gid']:
                if time.time() < cookie.get('expiry'):
                    return True
        return False
