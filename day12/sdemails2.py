import smtplib
import time
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders
from email.mime.base import MIMEBase

message = MIMEMultipart()
contrent = '''
     <h5>hello,贾经理</h5>
     <p>
         计算机测试报告：加减乘除功能..
     </p>
    '''
message.attach(MIMEText(contrent, 'html', 'utf-8'))
message['From'] = Header('关欣','utf-8')
message['To'] = Header('jason','utf-8')

subject = 'python邮件-%s' % time.ctime()
message['Subject'] = subject
file='calculator.html'
with open(file,'rb')as f:
    mime = MIMEBase('text', 'txt', filename=file)
    mime.add_header('Content-Disposition', 'attachment', filename=file)
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    message.attach(mime)

try:
    smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtpObj.login('565641627@qq.com', 'lceslynxpwzgbdae')
    smtpObj.sendmail('565641627@qq.com','13552648187@163.com', str(message))
    smtpObj.quit()
    print(u'邮件发送成功')
except smtplib.SMTPException as e:
    print(e)

#     sender = '565641627@qq.com'
#     receivers = '1051988636@qq.com'
#     cc_mail = '565641627@qq.com'
#     mail_pass = 'lceslynxpwzgbdae'
#     contrent = '''
#          <h5>hello,贾经理</h5>
#          <p>
#              计算机测试报告：加减乘除功能..
#          </p>
#         '''
# file = 'calculator.html'