m=1
n=3
while True:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
        
            break
    else:
        m=m+1
        if m==10001:
            print(n)
            break
    n+=1

