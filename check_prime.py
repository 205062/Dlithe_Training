n = int(input())
f=0

for i in range(2,n):
    if n%i == 0:
        print(False)
        f=1
        break

if f==0:
    print(True)