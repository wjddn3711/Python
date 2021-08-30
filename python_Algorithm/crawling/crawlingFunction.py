import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings(action='ignore')

# 대화 주제 1~ 75를 크롤링해서 리턴시키는 함수
def getSubject():
    targetSite = 'https://basicenglishspeaking.com/daily-english-conversation-topics/'
    request = requests.get(targetSite)
    # print(request) 성공
    html = request.text
    soup = BeautifulSoup(html, 'html.parser')

    subjects = []  # 파싱한 대화 주제를 저장할 빈 리스트
    divs = soup.findAll('div', {'class': 'tcb-col'})
    for div in divs:
        chapter = div.findAll('a')
        for a in chapter:
            subjects.append(a.text)
        #-===== for a
    #-=======for div
    return subjects

sub = getSubject()
for i in range(len(sub)):
    print('{0:2d}. {1}'.format(i+1,sub[i]))