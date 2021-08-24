
ar = list(map(int, input().split()))
rank = [1]*len(ar)
for i in range(len(ar)):
    for j in range(len(ar)):
        if ar[i]<ar[j]:
            rank[i]+=1
print(rank)