from unittest import TestCase
from appium import webdriver
from ddt import ddt
from ddt import data
from ddt import unpack
from initPage import Ininpaga
from LoginOperation import loginOpera
import time

@ddt
class TestLogin(TestCase):
    def setUp(self) -> None:
        url='127.0.0.1:4723/wd/hub'
        param={
            "platformName": "Android",
            "deviceName": "127.0.0.1:62001",
            "platformVersion": "7.1.2",
            "appPackage": "com.sina.weibo",
            "appActivity": "com.sina.weibo.SplashActivity"
        }
        self.driver=webdriver.Remote(url,param)
        time.sleep(8)

    def tearDown(self) -> None:
        self.driver.quit()

    @data(*Ininpaga.login_success_data)
    def testSuccessCase1(self,testdata):
        #提取数据
        username=testdata['username']
        password=testdata['password']
        expect=testdata['expect']

        #调用操作类
        loginobj=loginOpera(self.driver)
        loginobj.login(username,password)
        time.sleep(5)

        #获取实际结果
        data=loginobj.get_succes_data()

        #断言
        self.assertEqual(data,expect)

    @data(*Ininpaga.login_error_data)
    def testSuccessCase2(self, testdata):
        # 提取数据
        username = testdata['username']
        password = testdata['password']
        expect = testdata['expect']

        # 调用操作类
        loginobj = loginOpera(self.driver)
        loginobj.login(username, password)
        time.sleep(5)

        # 获取实际结果
        data = loginobj.get_error_data()

        # 断言
        self.assertEqual(data, expect)







