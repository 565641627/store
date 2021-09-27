import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
import unittest
tests=unittest.defaultTestLoader.discover(r'F:\pycharm\Pythonproject\day12',pattern='Testcalc*.py')
'''登录邮件服务器'''

sd=smtplib.SMTP_SSL('smtp.qq.com','465')#发件人邮箱的SMTP服务器
sd.login('565641627@qq.com','lceslynxpwzgbdae')#发件人的邮箱，密码
'''设置邮件内容'''
mail_body='''
    <h5>hello,贾经理</h5>
    <p>
        计算机测试报告：加减乘除功能..<a href="http://localhost:63342/day5.1.py/day12/%E8%AE%A1%E7%AE%97%E5%99%A8.html?_ijt=9n5uj0rjh0ukm48i6guq8k6v80&_ij_reload">这是测试报告</a></p>
    </p>

'''
mgy=MIMEText(mail_body,'html','utf-8')
mgy['From']=Header('关欣','utf-8')#发送者
mgy['TO']=Header('贾经理','utf-8')#接收者
mgy['Subject']=Header('计算器测试报告','utf-8')#主题
file='calculator.html'
# with open(file,'rb')as f:
#     mime=MIMEBase('text','txt',filename=file)
#     mime.add_header('Content-Disposition','attachment',filename=file)
#     mime.set_payload(f.read())
#     encoders.encode_base64(mime)
#     mgy.attach(mime)
'''发邮件'''
sd.sendmail('565641627@qq.com','2857070729@qq.com',mgy.as_string())

















