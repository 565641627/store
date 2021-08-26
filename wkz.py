a=input('请输入一个值：')
b=input('请输入一个值：')
c=input('请输入一个值：')
a=int(a)
b=int(b)
c=int(c)
if a==b==c:
    print('等边三角形')
elif a==b or a==c or b==c:
    print('等腰三角形')
elif a*a+b*b==c*c:
    print('直角三角形')
elif a+b>c and a+c>b and b+c>a:
    print('普通三角形')
else:
    print('不能构成三角形')