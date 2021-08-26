a='root'
b='admin'
c=3
while True:
    q=input('用户名')
    w = input('密码')
    c=c-1
    if c==0:
        print('GG!')
        break
    elif q!=a:
        print('ID mistake')
        continue
    elif w!=b:
        print('password mistake')
        continue
    else:
        print('OK!')
        break