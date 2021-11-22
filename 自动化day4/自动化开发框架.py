from HTMLTestRunner import HTMLTestRunner
from Email import send_mail
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="微博测试报告",
    description="微博页面测试报告",
    verbosity=1,
    stream=open(file="weibo.html", mode="w+", encoding="utf-8")
)

runner.run(tests)

# 4.任务： 使用邮件发送附件，把报告发送给我
send_mail('微博测试报告', 'V01', r'weibo.html', '2167365108@qq.com')  # 老贾:'2431320433@qq.com'
