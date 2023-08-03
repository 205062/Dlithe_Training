n = input().split()

for i in range(1,len(n)):
    val = n[i]
    j = i-1
    while j>=0 and n[j] > val:
        n[j+1] = n[j]
        j-=1
    n[j+1] = val

print(n)