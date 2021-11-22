from appium import webdriver
from unittest import TestCase
from InitPage import Initpage
from LoginWeibo import HomePage
from ddt import ddt
from ddt import data
import time


@ddt
class TestWeibo(TestCase):
    # 在所用用例执行之前
    def setUp(self) -> None:
        url = "127.0.0.1:4723/wd/hub"
        param = {
            "deviceName": "127.0.0.1:62001",
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "appPackage": "com.sina.weibo",
            "appActivity": "com.sina.weibo.SplashActivity"
        }
        self.driver = webdriver.Remote(url, param)
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]").click()
        time.sleep(6)

    @data(*Initpage.loginData)
    def testLogin(self, testdata):
        phone = testdata["phone"]
        password = testdata["password"]
        expect = testdata["expect"]

        login = HomePage(self.driver)
        # 执行登录操作获取结果
        result = login.login(phone, password)
        time.sleep(2)
        # # 获取实际结果
        # result = login.getLoginErrorResult()
        # 断言
        self.assertEqual(expect, result)

    @data(*Initpage.home)
    def testHome(self, testdata):
        expect = testdata['follow']
        login = HomePage(self.driver)
        # 执行首页操作获取结果
        result = login.home()
        time.sleep(3)
        self.assertEqual(expect, result)

    @data(*Initpage.home)
    def testVideo(self, testdata):
        expect = testdata['forward']
        login = HomePage(self.driver)
        # 执行视频操作获取结果
        result = login.video()
        time.sleep(3)
        self.assertEqual(expect, result)

    @data(*Initpage.home)
    def testDiscover(self, testdata):
        expect = testdata['search']
        login = HomePage(self.driver)
        # 执行视频操作获取结果
        result = login.discover()
        time.sleep(3)
        self.assertEqual(expect, result)

    @data(*Initpage.home)
    def testHelp(self, testdata):
        expect = testdata['help']
        login = HomePage(self.driver)
        # 执行视频操作获取结果
        result = login.news()
        time.sleep(3)
        self.assertEqual(expect, result)