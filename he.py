a=input("输入:")
a=int(a)
h=0
p=0
max=0
i=0
while i<9:
    a=input('输入:')
    a=int(a)
    h=h+a
    p=h/10
    i=i+1
    if a>max:
        max=a
    else:
        max=max
print('和',h)
print('平均数',p)
print('最大值',max)