data= [19,2,31,45,30,11,121,27]
mid = len(data)//2 # 정렬할 데이터의 중간 위치를 계산한다 => 블록의 크기

# 정렬할 데이터의 개수에 따라서 회전수가 달라지므로 정렬할 데이터의 중간 위치가 0보다 큰 동안 반복한다
while mid > 0:
    for i in range(mid,len(data)):
        key = data[i]
        index = i
        while index >= mid and data[index - mid] > key:
            data[index] = data[index - mid] # 값교환
            index -= mid
        # ====== while
        data[index] = key
    # ====== for => 회전 종료
    print(data)
    # 블록의 크기를 반으로 줄인다
    mid//=2
# ===== while => 정렬 종료
print(data)