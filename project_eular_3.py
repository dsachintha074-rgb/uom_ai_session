n=600851475143
k=0
for i in range(2,n):
    m=n%i
    if m==0:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            if i>= k:
                k=i
print(k)

