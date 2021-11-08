from HTMLTestRunner import HTMLTestRunner
import unittest

# 加载所有用例
tests = unittest.defaultTestLoader.discover(r'E:\python\python1\day13【单元测试】', pattern='Test*.py')

# 创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title='计算器的测试报告',
    description='这是加减乘除测试报告',
    verbosity=1,
    stream=open(file='计算器.html', mode='w+', encoding='utf-8')
)

# 执行用例
runner.run(tests)
