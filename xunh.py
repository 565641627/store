i=1
while i<=9:
    j=1
    while j<=i:
        print('%d*%d=%d'%(i,j,i*j),end=' ')
        j=j+1
    print(' ')
    i=i+1