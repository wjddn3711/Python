import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings(action='ignore')

# 1건의 대화 내용을 저장하는 클래스 => 질문과 답변이 한쌍으로 저장되는 클래스
class Conversation:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def __str__(self):
        return '질문: {}\n답변: {}'.format(self.question,self.answer)

# c=Conversation('who r u','none of ur business')
# print(c)

# 75개의 대화 주제와 세부 대화 내용의 url을 크롤링해서 리턴시키는 함수
def getSubject():
    targetSite = 'https://basicenglishspeaking.com/daily-english-conversation-topics/'
    request = requests.get(targetSite)
    # print(request) 성공
    html = request.text
    soup = BeautifulSoup(html, 'html.parser')

    subjects = []  # 파싱한 대화 주제를 저장할 빈 리스트
    contentLink = [] # 세부 대화 내용의 url 을 저장할 빈 리스트를 선언한다
    divs = soup.findAll('div', {'class': 'tcb-col'})
    for div in divs:
        chapter = div.findAll('a')
        for a in chapter:
            subjects.append(a.text)
            # 세부 대화 내용의 url을 리스트에 추가한다
            # print(a.get('href'))
            contentLink.append(a.get('href'))
    # 대화 주제와 대화 주제에 따른 세부 대화 내용의 url을 리턴시킨다
    # 리턴되는 데이터가 2개가 아니라 subjects, contentLink한개의 튜플로 리턴시킨다
    return subjects, contentLink

subjects, contents = getSubject()
# for i in range(len(subjects)):
#     print('{0:2d}. {1} - {2}'.format(i+1,subjects[i],contents[i]))

# 대화 주제에 따른 모든 대화 내용을 저장할 빈 리스트를 선언한다
conversations = [] # Convesation 클래스 객체를 저장한다

i = 0 # 대화 주제의 개수를 카운트 하는 변수 => 인덱스
# 대화 주제의 개수만큼 반복하며 각각의 대화 주제에 따른 대화 내용을 읽는다
for subject in subjects[:3]:
    conversations.append('{0:2d}. {1} - {2}'.format(i+1,subjects[i],contents[i]))
    # 대화 주제 1건이 처리완료 되면 다음 대화를 처리하기 위해서 i 를 1증가시킨다
    # 대화 주제별로 대화 내용을 크롤링할 페이지를 요청한다
    targetSite = contents[i]
    request = requests.get(targetSite)
    html = request.text
    soup = BeautifulSoup(html,'html.parser')
    # 대화 주제에 따른 대화 내용은 플레이 버튼(class 속성이 'sc_player_container1'인 div 태그)의 다음 형제이다
    divs = soup.findAll('div',{'class':'sc_player_container1'})
    # 각각의 대화 주제에 따른 문장의 개수만큼 반복한다
    for div in divs:
        # index() 메소드로 전체 중에서 인수로 지정한 객체의 index 번호를 얻어올 수 있다
        # divs.index(div) => 전체 버튼에서 (divs)에서 특정 버튼 (div)의 index 번호를 얻어온다
        # print(divs.index(div))
        # index() 메소드 실행 결과가 짝수면 질문이고 홀수면 답변이다

        # 크롤링할 데이터가 태그 내부에 작성된 것이 아니고 class 속성이 sc_player_container1인 div 태그의 다음 형제로 작성되어 있다
        # next_sibling => 다음 형제, previous_sibling => 이전 형제
        if divs.index(div)%2==0: # 질문인가?
            question = div.next_sibling
        else:
            answer = div.next_sibling

            # Conversation 클래스 객체를 만드는 작업은 질문과 답변이 한 쌍이 되는 순간 실행해야한다
            # 질문과 답변이 한 쌍이 되었으므로 Conversation 클래스 객체를 생성하고 질문과 답변을 저장한다
            c = Conversation(question,answer)
            # 질문과 답변이 한 쌍으로 저장된 Conversation 클래스 객체를 대화 내용을 기억하는 Conversation 리스트에 저장한다
            conversations.append(c)
    i+=1


for c in conversations:
    print(c)