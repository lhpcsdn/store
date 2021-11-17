from HTMLTestRunner import HTMLTestRunner
from Email import send_mail
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="HKR测试报告",
    description="hkr登录测试报告",
    verbosity=1,
    stream=open(file="hkr.html", mode="w+", encoding="utf-8")
)

runner.run(tests)

# 4.任务： 使用邮件发送附件，把报告发送给我
send_mail('hkr登录测试报告', 'V01', r'HKR.xlsx', '2167365108@qq.com')  # 老贾:'2431320433@qq.com'
