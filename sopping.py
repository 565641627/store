import random
dc= random.randint(0, 40)
if dc<10:
    dc=0.5
    print('恭喜获得联想优惠卷',dc)
elif 10<=dc<30:
    dc=0.6
    print('恭喜获得老干妈优惠卷',dc)
elif 30<dc<=40:
    dc=0.9
    print('恭喜获得乌江榨菜优惠卷',dc)


com=[
    ['联想电脑',4500],
    ['Mac Pc',12000],
    ['HUA WEI WATCH',1200],
    ['海尔洗衣机',5000],
    ['老干妈',15],
    ['乌江榨菜',1.5]
]
wallet=input('请初始化你的余额：')
wallet=int(wallet)
mycart=[]

while True:
    for key,value in enumerate(com):
        print(key,value)
    choes=input('请输入商品编号:')
    if choes.isdigit():
            choes=int(choes)
            if choes> len(com):
                print('该商品不存在，请重新输入：')
            else:
                if wallet<com[choes][1]:
                    print('穷鬼~')
                elif dc==0.5 and choes==0:
                    mycart.append(com[choes])
                    wallet = wallet - (com[choes][1])*0.5
                    print('恭喜，添加购物车成功！您的余额还剩：', wallet, '!')
                elif dc==0.6 and choes==4:
                    mycart.append(com[choes])
                    wallet = wallet - (com[choes][1])*0.6
                    print('恭喜，添加购物车成功！您的余额还剩：', wallet, '!')
                elif dc==0.9 and choes==5:
                    mycart.append(com[choes])
                    wallet = wallet - (com[choes][1])*0.9
                    print('恭喜，添加购物车成功！您的余额还剩：', wallet, '!')
                else:
                    mycart.append(com[choes])
                    wallet = wallet - (com[choes][1])
                    print('恭喜，添加购物车成功！您的余额还剩：',wallet,'!')
    elif choes =='q'or choes=='Q':
        print('欢迎下次光临！')
        break
    else:
        print('输入非法，请重新输入')

print('以下是你的购物萧条，请查收：')
print('----------------------------')
for key,value in enumerate(mycart):
    print(key,value)
print('您本次的月还剩￥',wallet)
print('----------------------------')