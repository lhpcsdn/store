from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginOpera:
    # 保证driver使用全局同一个
    def __init__(self, driver):
        self.driver = driver

    # 登陆
    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//*[@id='loginname']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)

        self.driver.find_element(By.XPATH, "//*[@id='submit']").click()

    # 获取登陆成功的实际结果
    def getLoginResult(self, expect):
        if expect == self.driver.title:
            return self.driver.title
        else:
            return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text

    # 获取失败的结果数据
    def getLoginErrorResult(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text
