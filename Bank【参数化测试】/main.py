'''
    1.加载所有的测试用例
    2.执行用例并生成测试报告
'''

import unittest
from Email import send_mail

# 1.加载所有用例
from HTMLTestRunner import HTMLTestRunner

tests = unittest.defaultTestLoader.discover(r"E:\python\python1\day14【参数化测试】", pattern="Test*.py")

# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="工商银行的的测试报告",
    description="工行测试报告",
    verbosity=1,
    stream=open(file="工商银行.html", mode="w+", encoding="utf-8")
)

# 3.执行用例
runner.run(tests)

# 4.任务： 使用邮件发送附件，把报告发送给我
send_mail('银行', 'V01', r'bank.xlsx', '2431320433@qq.com')  # 老贾:'2431320433@qq.com'
