import warnings
warnings.filterwarnings(action='ignore')
import datetime
import requests
from bs4 import BeautifulSoup
df=datetime.datetime.now()

targetSite='https://www.nate.com/'
request =requests.get(targetSite)
html=request.text
soup = BeautifulSoup(html,'html.parser')
# print(request)


# 순위
ranks = soup.findAll('span', {'class':'num_rank'})
# print(ranks)
# for rank in ranks[:5]:
#     print(rank.text)


# 실시간 이슈 키워드와 상승/히릭 폭 크롤링
issues = soup.findAll('a',{'class':'ik'})
# for issue in issues:
#     print(issue.text.strip().split('\n')[0],issue.text.strip().split('\n')[1])

for i in range(5):
    rank = ranks[i].text
    issue = issues[i].text.strip().split('\n')[0]
    upDown = issues[i].text.strip().split('\n')[1]
    print('{0:>2s}위: {1}'.format(rank,issue), end=' ')
    if '상승' in upDown:
        print('[{}{}]'.format('^',upDown[2:]))
    elif '하락' in upDown:
        print('[{}{}]'.format('-',upDown[2:]))
    elif '동' in upDown:
        print('[{}{}]'.format('=',upDown[2:]))
    else:
        print('[+]')