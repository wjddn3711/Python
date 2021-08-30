import requests
from bs4 import BeautifulSoup

targetSite = 'https://basicenglishspeaking.com/daily-english-conversation-topics/'
request = requests.get(targetSite)
# print(request) 성공
html = request.text
soup = BeautifulSoup(html,'html.parser')

subjects = [] # 파싱한 대화 주제를 저장할 빈 리스트
divs = soup.findAll('div',{'class':'tcb-col'})
for div in divs:
    chapter = div.findAll('a')
    for a in chapter:
        # print(a.text)
        subjects.append(a.text)
for i in range(len(subjects)):
    print('{}. {}'.format(i+1,subjects[i]))