ar = list(map(int,input().split()))
for i in range(len(ar)-1):
    for j in range(i+1,len(ar)):
        if ar[j] > ar[i]:
            ar[j],ar[i]=ar[i],ar[j]
print(ar)