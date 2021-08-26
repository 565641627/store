import random
num = random.randint(0, 50)
m = 100
while True:
    a = input('请输入一个数字：')
    a = int(a)
    m = m-10
    if m==0:
        print('low b')
        break
    elif a == num:
        print('victory', m)
        break
    elif a < num:
        print('太小',m)
    else:
        print('太大',m)



