import warnings
warnings.filterwarnings(action='ignore')
import datetime
import json # json 형태의 문자열을 파이썬에서 처리하기 위해 loads() 메소드로 딕셔너리나 리스트 형태로 변환한다
import requests
# from bs4 import BeautifulSoup # html 문서를 파싱할 때 사용하므로 AJAX로 넘어오는 데이터를 크롤링 할 때 사용하지 않는다

# 실시간 검색어가 웹 페이지에 전부 혹은 일부가 포함되어있지 않고 AJAX 를 이용해서 받아오는 방식이 사용된다
# Request Method 가 GET 이므로 requests 모듈의 get() 메소드를 사용해서 실시간 검색어을 받아온다
targetSite='https://www.nate.com/js/data/jsonLiveKeywordDataV1.js?v=202109062010'
request =requests.get(targetSite)
# print(request)
issues = request.text
# print(type(issues)) str 형태
# 파이썬은 한글 encoding 이 유니코드(UTF-8) 로 되어있기 때문에 encoding이 'euc-kr' 등의 방식으로 되어있을 경우 사이트를
# 크롤링 할 때 한글이 깨져서 보이면 아래와 같이 한글 encoding 을 바꿔준다
request.encoding = 'euc-kr'
# json 문자열 형태로 얻어온 실시간 이슈 키워드는 json 모듈의 loads() 메소드를 사용해서 파이썬에서
# 처리할 수 있는 데이터 타입으로 변환시켜 처리한다
# loads() 메소드는 json 타입의 문자열이 {}를 포함하는 형태면 딕셔너리로 []만 포함하는 형태면 리스트로 자동 변환한다
ranks = json.loads(issues)
# print(type(ranks))
# print(ranks)
# json 모듈을 사용하지 않으려면 requests 모듈의 json()메소드를 사용해서 파이썬에서 처리할 수 있는 데이터
# 타입으로 변환시켜 사용한다
# ranks = request.json()
# print(type(ranks))
# print(ranks)
for i in range(10):
    upDown = ranks[i][2]
    print('{0:>2s}위 {1}'.format(ranks[i][0],ranks[i][1]), end=' ')
    if upDown == 's':
        print('[{}]'.format('='))
    elif upDown == 'n':
        print('[{}]'.format('+'))
    elif upDown == '+':
        print('[{}]'.format(upDown+ranks[i][3]))
    else:
        print('[{}]'.format(upDown+ranks[i][3]))