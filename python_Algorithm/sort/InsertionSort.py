ar = [8,3,4,9,1]
n=len(ar)
for i in range(1,n):
    key = ar[i]
    index = i
    for j in range(i-1,-1,-1):
        if ar[j]>key:
            ar[j+1]=ar[j]
        else:
            break
    ar[i]=key
print(ar)