n=0
k=0
for i in range(100,1000):
    for j in range(100,1000):
        n=i*j
        m=str(n)
        if m==m[::-1]:
            if n>=k:
                k=n
print(k)


