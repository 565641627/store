i=9
while i>=1:
    j=1
    while j<=i:
        print('%d*%d=%d'%(i,j,i*j),end=' ')
        j=j+1
    print(' ')
    i=i-1