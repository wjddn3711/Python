# 큐로 사용할 비어있는 2차원 리스트 만들기
# queueList = [[] for _ in range(10)]

ar=[19,2,31,45,30,11,121,27]
isSort = False # 정렬이 완료되었나 기억하는 변수, True 로 변경되면 정렬이 완료되었음을 의미한다
radix = 1 # 큐에 넣어줄 자리수의 위치를 기억하는 변수, 1=> 10 => 100 => 1000....
while not isSort:
    isSort = True
    # 정렬할 숫자의 기수(진법)의 크기만큼 큐로 사용할 리스트를 만든다
    queueList = [[] for _ in range(10)]
    print('radix: {}'.format(radix))
    for i in range(len(ar)):
        print('n: {0:3d}'.format(ar[i]),end=' =>')
        # 큐에 넣어줄 자리수에 해당하는 숫자만 뽑아낸다
        digit = ar[i]//radix % 10
        print(digit)
        # 큐에 숫자를 넣어준다
        queueList[digit].append(ar[i])
        # 정렬이 완료되었나 검사한다
        if isSort and digit > 0: #불필요한 비교를 막기 위해 isSort조건을 추가했다
            isSort = False
    # === for
    # 큐에 저장된 데이터를 0번 큐의 데이터부터 차례대로 꺼내서 ar 리스트에 다시 저장한다
    index = 0
    # queList 에 저장된 0번 큐를 numbers 리스트에 저장한 다음 반복을 시작해서 9번 큐를 numbers 리스트에 저장한 후 반복한
    # 다음 종료한다
    for numbers in queueList:
        # 각각의 큐에 해당되는 리스트에 저장된 데이터 개수만큼 반복하며 data 리스트를 수정한다
        for number in numbers:
            ar[index] =number
            index +=1
        # ==== for
    # ==== for
    print(ar)
    print('='*80)
    #다음 자리수를 큐에 넣기 위해서 radix에 저장된 숫자에 10을 곱한다
    radix *=10
#===== while