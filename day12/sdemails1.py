import smtplib
import time
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders
from email.mime.base import MIMEBase
from email.utils import parseaddr,formataddr
from email.mime.image import MIMEImage

def Sendmail(sender,receivers,cc_mail,mail_pass,content,file):
    mail_host = "smtp.qq.com"
    message = MIMEMultipart()
    message.attach(MIMEText(content,'html','utf-8'))
    message['From']=sender
    message['To']=','.join(receivers)
    message['From']=','.join(cc_mail)

    subject = 'python邮件-%s' % time.ctime()
    message['Subject']=subject

    with open(file,'rb') as f:
        mime = MIMEBase('text','txt',filename=file)
        mime.add_header('Content-Disposition','attachment',filename=file)
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        message.attach(mime)

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host,465)
        smtpObj.login(sender,mail_pass)
        smtpObj.sendmail(sender,receivers,str(message))
        smtpObj.quit()
        print(u'邮件发送成功')
    except smtplib.SMTPException as e:
        print(e)

if __name__ == '__main__':
    sender = '565641627@qq.com'
    receivers = '1051988636@qq.com'
    cc_mail = '565641627@qq.com'
    mail_pass='lceslynxpwzgbdae'
    contrent='''
     <h5>hello,贾经理</h5>
     <p>
         计算机测试报告：加减乘除功能..
     </p>
    '''
file='calculator.html'
Sendmail(sender,receivers,cc_mail,mail_pass,contrent,file)









