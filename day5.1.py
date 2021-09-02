info='''("==============================================")
("|------------中国工商银行账户管理系统------------|")
("|------------1、开户              ------------|")
("|------------2、取钱              ------------|")
("|------------3、存钱              ------------|")
("|------------4、转账              ------------|")
("|------------5、查询              ------------|")
("|------------6、退出              ------------|")
("==============================================")'''
print(info)
import random
bank={}
bank_name='工商银行巴戈亚路分行'
def bank_adduser(account,username,password,country,province,street,hnr):
    if len(bank) > 100:
        return 3
    if username in bank:
        return 2
    bank[username]={
        'account':account,
        'password':password,
        'country':country,
        'province':province,
        'street':street,
        'hnr':hnr,
        'money':0,
        'bank_name':bank_name
    }
    return 1
def adduser():
    username = input('请输入您的用户名')
    password=int(input('请输入密码'))
    print('请输入您的地址：')
    country=input('\t\t请输入你所在的国家')
    province=input('\t\t请输入你所在的省份')
    street=input('\t\t请输入你所在的街道')
    hnr=input('\t\t请输入你的门牌号')
    account=random.randint(10000000,99999999)
    id=bank_adduser(account,username,password,country,province,street,hnr)
    if id == 1:
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
        print(info % (username, account, country, province, street, hnr, bank[username]["money"], bank_name))
    if id ==2:
        print('用户已存在')
    if id ==3:
        print('用户已满，添加失败！')

def addduser():
    username=input('请输入你的用户名')
    while True:
        if  username not in bank:
            print('用户名不存在')
            break
        else:
            amout = int(input('请输入你要存入的金额'))
            bank[username]['money']=bank[username]['money']+amout
            print('恭喜存钱成功，您的余额为：',bank[username]['money'])
            return
def adddduser():
    info = input('请输入你的用户名')
    for i in bank:
        if i==info:
            while True:
                password = int(input('请输入你的密码：'))
                if password != bank[i]['password']:
                    print('密码错误,请重新输入密码:')
                else:
                    amout = int(input('请输入你要取出的金额'))
                    if amout>bank[i]['money']:
                        print('余额不足')
                        break
                    else:
                        bank[i]['money']-=amout
                        print('恭喜取钱成功，您的余额为：', bank[i]['money'])
                        return
        else:
            print('用户名不存在')

def transfer():
    anm=int(input('请输入账号：'))
    for i in bank:
        if bank[i]['account'] == anm:
                anmm = int(input('请输入转入账号：'))
                for y in bank:
                    if bank[y]['account']==anmm:
                        while True:
                            password=int(input('请输入密码:'))
                            if password !=bank[i]['password']:
                                print('密码错误请重新输入：')
                            else:
                                tfm=int(input('请输入转账金额:'))
                                while True:
                                    if tfm>bank[i]['money']:
                                        print('余额不足')
                                        break
                                    else:
                                        bank[i]['money']-=tfm
                                        bank[y]['money']+=tfm
                                        print('转账成功,您的余额为：',bank[i]['money'])
                                        return
    else:
        print('账号不存在')

def query():
    anm=int(input('请输入账号:'))
    for i in bank:
        if bank[i]['account']==anm:
            pwd=int(input('请输入密码'))
            print(bank[i])
            if bank[i]['password']!=pwd:
                print('密码错误')
            else:
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
                print(info % (i, bank[i]['account'],bank[i]['country'],bank[i]['province'], bank[i]['street'],bank[i]['hnr'], bank[i]["money"], bank_name))
                return
    else:
        print('账号不存在')

while True:
    select=input('请选择您想要办理的业务')
    if select=='1':
        print('开户')
        adduser()
    elif select=='2':
        print('取钱')
        adddduser()
    elif select=='3':
        print('存钱')
        addduser()
    elif select=='4':
        print('转账')
        transfer()
    elif select == '5':
        print('查询')
        query()
    elif select == '6':
        print('退出')
        break