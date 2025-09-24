m=0
n=0
for i in range(1,101):
    m=m+i**2
for j in range(1,101):
    n=n+j
n=n**2
print(n-m)