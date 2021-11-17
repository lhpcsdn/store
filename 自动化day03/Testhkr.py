from selenium import webdriver
from unittest import TestCase
from write import get_write
from write import get_data
from ddt import ddt
from ddt import data
from InitPage import InitPage
from LoginOperation import LoginOpera
import time


@ddt
class TestHkr(TestCase):
    # 在所有用例执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/HKR")
        self.driver.maximize_window()

    # 在所有用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()

    @data(*get_data('HKR.xlsx', 'LoginOperation'))
    def testLoginSuccess(self, testdata):

        username = testdata[0]
        password = testdata[1]
        expect = testdata[2]
        row = testdata[3]

        login = LoginOpera(self.driver)

        # 执行登陆的三项操作
        login.login(username, password)

        # 获取实际结果
        result = login.getLoginResult(expect)

        if result == expect:
            get_write('HKR.xlsx', 'LoginOperation', row, 3, '通过', 'HKR.xlsx')
        else:
            get_write('HKR.xlsx', 'LoginOperation', row, 3, '不通过', 'HKR.xlsx')

        time.sleep(2)

        # 断言
        self.assertEqual(expect, result)

    # @data(*InitPage.loginErrorData)
    # def testLoginError(self, username, password, expect):
    #     username = username
    #     password = password
    #     expect = expect
    #
    #     login = LoginOpera(self.driver)
    #
    #     # 执行登陆的三项惭怍
    #     login.login(username, password)
    #
    #     # 获取实际结果
    #     result = login.getLoginErrorResult()
    #
    #     time.sleep(3)
    #
    #     # 断言
    #     self.assertEqual(expect, result)
