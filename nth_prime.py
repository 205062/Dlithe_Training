n = int(input())
f=0
c = 1
k=3
while(c!=n):
    for i in range(2,k//2 + 1):
        if k%i == 0:
            f = 1
            break
    if f == 0:
        c+=1
    f=0
    k+=1
print(k-1)