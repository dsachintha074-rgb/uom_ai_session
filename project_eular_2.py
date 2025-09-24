u=0
v=1
w=0
sum=0
while u+v<4000000:
    w=u+v
    u=v
    v=w  
    if w%2==0:
        sum=sum+w
print(sum)
