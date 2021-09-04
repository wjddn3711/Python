# !pip install requests # 크롤링할 사이트에 접속해서 html 문서를 읽어 온다
# !pip install beautifulsoup4 # requests 모듈을 사용해서 읽어온 html 문서를 파싱(분석)한다
import requests
from bs4 import BeautifulSoup
# 경고 메시지가 출력되지 않게 하려면 아래 코드를 실행한다
# 다시 경고 메시지가 출력되게 하려면 action='default' 로 수정하여 실행
import warnings
warnings.filterwarnings(action='ignore')
# 실시간으로 크롤링한 시간대를 알기 위해 데이트타임 사용
import datetime
df=datetime.datetime.now()


targetSite='https://search.musinsa.com/ranking/best'
header = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
# requests 모듈의 get() 메서드로 타켓 사이트의 정보를 얻어온다. 요청한다
request =requests.get(targetSite, headers=header)
# 406(허용되지 않음): 요청한 페이지가 요청한 콘텐츠 특성으로 응답할 수 없다 헤더를 사용하여 406 에러 피하기!
# 200(성공): 서버가 요청을 제대로 처리했다는 뜻으로 주로 서버가 요청했다는 페이지를 제공했다는 의미로 쓰인다
# print(request) # 200 이 뜨면 정상
# 타켓 사이트에서 얻어온 정보 중에서 text로 된 html문서를 얻어온다
html=request.text
# print(html)
# bs4 모듈의 BeautifulSoup() 함수로 타켓 사이트에서 얻어온 html 문서를 html parser를 사용해 파싱할 수 있도록 준비한다
soup = BeautifulSoup(html,'html.parser')
# titles = soup.findAll('div', {'class':'ellipsis rank01'})

# 무신사 사이트에서 크롤링한 브랜드를 저장할 변수
brands = soup.findAll('p', {'class':'item_title'})
# for item in brands:
#     print(item.text.strip())

# 무신사에서 크롤링한 의류이름을 저장할 변수
items = soup.findAll('p',{'class':'list_info'})


start=0 # 유효 인덱스를 저장할 변수
cnt = 1 # 순위를 나타낼 변수
itemList = [] # 최종 순위, 의류이름 을 저장할 리스트
for item in items:
    # print(item.text.split())
    list = item.text.split()
    if '배송' in list : # 만약 배송이 포함 되어 있다면 '배송'을 기준으로 배송 뒤까지를 저장
        start = list.index('배송') +1
        # print(cnt, *list[start:])
        itemList.append((cnt,''.join(list[start:])))
        cnt+=1
    elif '새벽배송' in list: # 만약 새벽배송이 포함 되어 있다면 '새벽배송'을 기준으로 배송 뒤까지를 저장
        start = list.index('새벽배송') + 1
        # print(cnt, *list[start:])
        itemList.append((cnt,''.join(list[start:])))
        cnt += 1
    else: # 배송이 포함되어있지 않은 경우
        # print(cnt, *list)
        itemList.append((cnt,''.join(list)))
        cnt+=1

# for i in range(90):
#     print('{0:2d}위 브랜드:{1:10s} 상품:{2}'.format(itemList[i][0],brands[i].text.strip(),itemList[i][1]) )

file = open('./output/musinsaTOP90.txt','w')
file.write('{} 현재 무신사 실시간 TOP 90\n'.format(df))
for i in range(90):
    file.write('{0:2d}위 브랜드:{1:10s} 상품:{2}\n'.format(itemList[i][0],brands[i].text.strip(),itemList[i][1]) )
file.close()
print('musinsaTOP90.txt 쓰기 완료')

# text 파일에 저장된 데이터를 읽어서 화면에 출력한다
try:
    file = open('./output/musinsaTOP90.txt', 'r')
    lines = file.readlines()
    for line in lines:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print('디스크에 musinsa90.txt 파일이 없습니다')

