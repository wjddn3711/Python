
n = int(input())
ar = [ int(input()) for _ in range(n)]
for i in range(len(ar)-1):
    cnt = 0
    for j in range(len(ar)-i-1):
        if ar[j] > ar[j+1]:
            ar[j],ar[j+1] = ar[j+1],ar[j]
            cnt+=1
    if cnt==0: break

[print(ar[i]) for i in range(len(ar))]