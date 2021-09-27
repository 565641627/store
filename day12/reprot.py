from HTMLTestRunner import HTMLTestRunner
import unittest
tests=unittest.defaultTestLoader.discover(r'F:\pycharm\Pythonproject\day12',pattern='Testcalc*.py')
runner=HTMLTestRunner.HTMLTestRunner(
    title='这是一份计算器的测试报告',
    description='这是加减乘除功能的测试报告',
    verbosity=1,
    stream=open('calculator.html',mode='w+',encoding='utf-8')
)

runner.run(tests)







