
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")







import random
import datetime

import pymysql

con = pymysql.connect(host="localhost", user='root', password="", database='bank', charset='utf8')

cursor = con.cursor()

def amunt():

    username=input('请输入您的用户名')
    amunt=input('请输入您要存入的金额')


    sql = "update user set money=money+"+amunt+" where username=%s"

    a = [username]

    cursor.execute(sql,a)
    con.commit()

    sql2 = "select money from user where username = %s"
    b = [username]
    cursor.execute(sql2,b)
    money = cursor.fetchmany(1)
    con.commit()
    print(money)





def usermoney():

    username=input('请输入您的用户名')
    password = input('输入密码')
    usermoney = input('输入取款金额')
    sql = "update user set money=money-"+usermoney+" where username=%s and password="+password+""
    a = [username]
    cursor.execute(sql,a)
    con.commit()
    cursor.execute("select money from user where username = "+username+"")
    money = cursor.fetchmany(1)
    print(money)



def search():
    username = input('请输入用户名')



    sql = "select * from `user` where username = %s"
    param = [username]

    cursor.execute(sql, param)

    data = cursor.fetchone()

    for i in data:
        print(i)

    con.commit()

    cursor.close()
    con.close()


def transfer():
    username1= input('请输入付款账户')
    password= input('请输入密码')
    username2= input('请输入收款账户')
    money1=input('请输入转账金额')
    sql1 = "update users set money=money-%s where username=%s and password=%s"
    a =[money1,username1,password]
    cursor.execute(sql1, a)
    sql2 = "update users set money=money+%s where username=%s"
    b = [money1, username2]
    cursor.execute(sql2,b)
    con.commit()
    sql3 = "select money from users where username=%s"
    b = [username1]
    cursor.execute(sql3,b)
    money2 = cursor.fetchmany(1)
    print("付款账户余额为：",money2)
    sql4 = "select money from users where username=%s"
    b = [username2]
    cursor.execute(sql4,b)
    money3 = cursor.fetchmany(1)
    print("收款账户余额为：",money3)





def adduser():
    username=input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    account=random.randint(10000000,99999999)
    money = 0
    registerDate = datetime.datetime.now()
    bankname = "工商银行七马路分行"

    # con = pymysql.connect(host="localhost", user='root', password="", database='bank',charset='utf8')
    #
    # cursor = con.cursor()

    sql = "insert into  user value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = [account, username, password, country, province, street, door, money, registerDate, bankname]



    cursor.execute(sql,param)

    con.commit()

    cursor.close()
    con.close()
    print("恭喜你开户成功下面是你的信息")
    info = '''
                       ------------个人信息------------
                       用户名:%s
                       账号：%s
                       密码：*****
                       国籍：%s
                       省份：%s
                       街道：%s
                       门牌号：%s
                       余额：%s
                       开户行名称：%s
                   '''

    print(info % (username, account, country, province, street, door, money, bankname))



while True:
    begin=input("请选择业务")
    if begin == "1":
        print("1、开户")
        adduser()
    elif  begin == "2":
        print("2、取钱")
        usermoney()
    elif  begin == "3":
        print("3、存钱")
        amunt()
    elif  begin == "4":
        print("4、转账")
        transfer()
    elif  begin == "5":
        print("5、查询 ")
        search()
    elif begin == "6":
        print("6、退出")
        break