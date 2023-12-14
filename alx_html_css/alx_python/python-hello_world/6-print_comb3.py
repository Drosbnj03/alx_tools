for i in range(0,10):
    for j in range(i+1,10):
        if i!=j:
            if str(i)+str(j) =='89':
                print(89)
            else:    
                print('{}{}'.format(i,j),end = ", " )