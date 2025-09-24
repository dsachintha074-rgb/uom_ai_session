m=2
n=3
while n<2000000:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            break
    else:
        m=m+n
    n=n+1
print(m)