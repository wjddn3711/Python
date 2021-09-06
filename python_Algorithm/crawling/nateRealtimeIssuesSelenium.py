# selenium 을 사용하기 위해 selenium 을 설치하고 import 한다
# !pip install selenium

import warnings
warnings.filterwarnings(action='ignore')
# import requests # selenium을 사용해서 웹 페이지의 내용을 얻어올 것이므로 사용하지 않는다
from bs4 import BeautifulSoup
from selenium import webdriver
# selenium 을 사용해 가상 크롬을 실행한다 => 사용중인 크롬 버전(93.0.4577.63)과 같은 버전의 크롬 드라이버를 OS에 맞게 다운받는다
# 다운받은 크롬 드라이버를 현재 소스파일이
driver = webdriver.Chrome('/Users/jungwoo/Desktop/crawling/chromedriver')
# get() 메소드로 가상 크롬에 크롤링할 타겟 사이트를 띄운다
driver.get('https://www.nate.com/')
html = driver.page_source
# print(html)
soup = BeautifulSoup(html,'html.parser')
ranks = soup.findAll('span', {'class':'num_rank'})


# 실시간 이슈 키워드와 상승/히릭 폭 크롤링
issues = soup.findAll('a',{'class':'ik'})

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