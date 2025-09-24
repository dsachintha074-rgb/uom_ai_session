for i in range(1,1000):
    for j in range(1,1000):
        for k in range(1,1000):
            if i**2+j**2==k**2 and i+j+k==1000 and i<j<k :
                print(i*j*k)
                break