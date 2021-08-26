for i in range(8):
    for j in range(0,8-i):
        print(end=' ')
    for k in range(8-i,8):
        print('*',end=' ')
    print('')