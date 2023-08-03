s = int(input())
e = int(input())
n = int(input())
f=0
c = 0
k=s
while(c!=n and k<e):
    for i in range(2,k//2 + 1):
        if k%i == 0:
            f = 1
            break
    if f == 0:
        c+=1
    f=0
    k+=1
if k==e:
    print(k)

else:
    print(k-1)