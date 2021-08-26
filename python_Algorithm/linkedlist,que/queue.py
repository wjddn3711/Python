class Queue:
    def __init__(self, size=5):
        self.queue = []  # 큐 => 빈 리스트 => append() 메소드로 데이터 추가
        self.size = size  # 큐의 크기
        self.rear = 0  # 큐의 뒤쪽 포인터 => 큐에 데이터가 입력될 때 마다 1씩 증가한다.
        self.front = 0  # 큐의 앞쪽 포인터 => 큐에서 데이터가 제거될 때 마다 1씩 증가한다

    # add => 입력
    def add(self, data):
        # 큐에 중복되는 데이터의 입력을 허용하지 않는다.
        if data in self.queue:  # 입력하려는 데이터가 큐에 존재하는가?
            # 추가하려는 데이터가 큐에 존재하기 때문에 중복되는 데이터라고 메시지를 출력한다.
            print('{}는(은) 중복되는 데이터입니다.'.format(data))
        else:
            # 큐에 추가하려는 데이터가 큐에 존재하지 않으므로 큐에 데이터를 추가한다.
            # 데이터를 추가하기 전에 overflow 인가 검사한다.
            # 큐의 크기(self.size)가 5일 때 큐로 사용할 리스트의 인덱스(self.rear)는 0, 1, 2, 3, 4만 사용할 수 있다.
            if self.size > self.rear:
                # overflow가 발생되지 않았으므로 큐에 데이터를 저장한다.
                self.queue.append(data)
                # 큐에 데이터를 저장했으므로 rear를 1증가시킨다.
                self.rear += 1
                print('큐에 {}을(를) 저장합니다.'.format(data), end=' ')
                print('rear = {}, front = {}'.format(self.rear, self.front))
            else:
                # overflow가 발생되면 큐가 가득찼다는 메시지를 출력한다.
                print('overflow 발생... 큐가 가득차서 {}를(을) 저장할 수 없습니다.'.format(data))
            # ===== if
        # ===== if
        # 큐에 저장된 데이터를 출력하는 함수를 실행한다.
        # 현재 클래스의 다른 함수를 실행할 때는 반드시 앞에 'self.'을 붙여서 실행해야 한다.
        self.view()
    def remove(self):
        # underflow 인가 검사한다
        if self.rear <= 0 or self.rear == self.front:
            print('큐에 저장된 데이터가 없습니다')
        else:
            data = self.queue[self.front] # 큐에 저장된 제거할 데이터를 얻어온다
            self.queue[self.front] = '' # 얻어온 데이터를 큐에서 제거한다
            self.front +=1 # 데이터를 제거했으므로 front 를 1증가시킨다
            print('큐에서 제거된 데이터: {}'.format(data), end=' ')
            print('rear = {}, front = {}'.format(self.rear, self.front))
            self.view()

    # remove => 출력

    # view => 보기
    def view(self):
        # 큐에 저장된 데이터를 출력한다.
        print('큐에 저장된 데이터 => ', end='')
        # underflow 인가 검사한다.
        # 1. 큐에 데이터가 1건도 입력되지 않았을 경우 rear가 0이므로 underflow가 발생된다
        # 2. 큐에 데이터가 입력된 후 입력된 데이터가 모두 제거되면 rear와 front가 같아지면서 underflow 가 발생된다
        if self.rear <= 0 or self.rear == self.front:
            # 큐에 저장된 데이터가 없으므로 없다고 출력한다.
            print('없음', end='')
        else:
            # 큐에 저장된 데이터의 개수만큼 반복하며 큐에 저장된 데이터를 출력한다.
            for i in range(self.front, self.rear):
                print(self.queue[i], end=' ')
        # ===== if
        print()
queue = Queue()
queue.view()
queue.remove()
queue.add(111)
queue.add(111)
queue.add(888)
queue.add(222)
queue.remove()
queue.remove()
queue.remove()
