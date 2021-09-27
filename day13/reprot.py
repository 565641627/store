from HtmlTestRunner import HTMLTestRunner
import unittest
tests=unittest.defaultTestLoader.discover(r'F:\pycharm\Pythonproject\day13',pattern='Test*.py')
runner=HTMLTestRunner.HTMLTestRunner(
    title='这是一份工商银行的测试报告',
    description='这是主要功能的测试报告',
    verbosity=1,
    stream=open('ICBCTest_report.html', mode='w+', encoding='utf-8')
)

runner.run(tests)