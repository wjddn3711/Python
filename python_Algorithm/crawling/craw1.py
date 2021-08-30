# 경고 메시지가 출력되지 않게 하려면 아래 코드를 실행한다
import warnings
warnings.filterwarnings(action='ignore')
# 다시 경고 메시지가 출력되게 하려면 action='default' 로 수정하여 실행

# 크롤링에 사용할 라이브러리를 설치하고 import gksek
# !pip install requests # 크롤링할 사이트에 접속해서 html 문서를 읽어 온다
# !pip install beautifulsoup4 # requests 모듈을 사용해서 읽어온 html 문서를 파싱(분석)한다
import requests
from bs4 import BeautifulSoup

targetSite = "http://dowellcomputer.com/main.jsp"
# requests 모듈의 get() 메서드로 타켓 사이트의 정보를 얻어온다. 요청한다
request = requests.get(targetSite)
# 200(성공): 서버가 요청을 제대로 처리했다는 뜻으로 주로 서버가 요청했다는 페이지를 제공했다는 의미로 쓰인다
# print(request) # 200 이 뜨면 정상
# 타켓 사이트에서 얻어온 정보 중에서 text로 된 html문서를 얻어온다
html = request.text
# print(html)
# print(type(html))

# bs4 모듈의 BeautifulSoup() 함수로 타켓 사이트에서 얻어온 html 문서를 html parser를 사용해 파싱할 수 있도록 준비한다
soup = BeautifulSoup(html,'html.parser')
# print(type(soup))
# print(soup)

# html 태그와 html 태그에 지정한 속성을 이용한 크롤링
# findall('태그이름',{'속성이름':'속성값',...,}) => 속성없이 태그 단위로만 크롤링할 때는 {} 안의 내용을 생략할 수 있다

# 최근 공지사항은 <b> 태그 내부에 있다
# notices = soup.findAll('b')
# for item in notices:
#     print(item.text)
#컴잘알에 오신 것을 환영합니다.
# C언어 기초 프로그래밍 강좌 20강 - 동적 메모리의 활용 (C Programming Tutorial For Beginners 2017 #20)
# C언어 기초 프로그래밍 강좌 19강 - 동적 메모리 (C Programming Tutorial For Beginners 2017 #19)
# C언어 기초 프로그래밍 강좌 18강 - 파일 입출력 (C Programming Tutorial For Beginners 2017 #18)
# C언어 기초 프로그래밍 강좌 17강 - 구조체의 활용 ② (C Programming Tutorial For Beginners 2017 #17)
# C언어 기초 프로그래밍 강좌 16강 - 구조체의 활용 ① (C Programming Tutorial For Beginners 2017 #16)

# 최근 공지사항은 class 속성이 'tail'인 <td> 태그 내부에 있다
# notices = soup.findAll('td',{'class':'tail'})
# print(notices)
# for notice in notices:
    # print(notice.text)

# CSS 선택자를 이용한 크롤링
# 자식 선택자 ('>') 또는 자식 선택자 ('' => 공백)를 이용한 크롤링
# select('CS 선택자')
# 최근 공지사항은 href 속성의 속성값 중에 'notice'라는 문자열이 포함되어있는 <a> 태그 내부에 있다
# notices = soup.select('td > a')
for notice in notices:
    # print(notice)
    # get() 메소드로 인수로 지정한 속성의 값을 얻어온다
    # print(notice.get('href'))
    # href 속성값 중에서 'notice' 가 포함된 요소만 얻어온다
    if 'notice' in notice.get('href'):
        print(notice.text)