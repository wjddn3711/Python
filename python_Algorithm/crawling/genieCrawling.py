import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings(action='ignore')
import datetime
df=datetime.datetime.now()

# # 타겟 사이트 주소 만들기
# # https://www.genie.co.kr/chart/top200?ditc=D&ymd=20210901&hh=20&rtm=Y&pg=1 -1~50
# # https://www.genie.co.kr/chart/top200?ditc=D&ymd=20210901&hh=20&rtm=Y&pg=2 -51~100
# # https://www.genie.co.kr/chart/top200?ditc=D&ymd=20210901&hh=20&rtm=Y&pg=3 -101~150
# # https://www.genie.co.kr/chart/top200?ditc=D&ymd=20210901&hh=20&rtm=Y&pg=4 -151~200
# url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20210901&hh=20&rtm=Y&pg='
# tt = []
# for i in range(1,3):
#     # targetSite = url + str(i)
#     targetSite = '{}{}'.format(url,i)
#     # print(targetSite)
#     header = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
#     request =requests.get(targetSite, headers=header)
#     html=request.text
#     soup = BeautifulSoup(html,'html.parser')
#     titles = soup.findAll('a', {'class': 'title ellipsis'})
#     for title in titles:
#         tt.append(title.text.strip())
# print(len(tt))
# art =[]
# for i in range(1,3):
#     # targetSite = url + str(i)
#     targetSite = '{}{}'.format(url,i)
#     # print(targetSite)
#     header = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
#     request =requests.get(targetSite, headers=header)
#     html=request.text
#     soup = BeautifulSoup(html,'html.parser')
#     artists = soup.findAll('a', {'class': 'artist ellipsis'})
#     for a in artists[5:]:
#         art.append(a.text)

genie = []
header = {"User-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20210901&hh=20&rtm=Y&pg='
for i in range(1,5):
    # targetSite = url + str(i)
    targetSite = '{}{}'.format(url,i)
    # print(targetSite)
    request =requests.get(targetSite, headers=header)
    html=request.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.findAll('a', {'class': 'title ellipsis'})
    artists = soup.findAll('a', {'class': 'artist ellipsis'})

    for j in range(50):
        genie.append((artists[j+5].text.strip(),titles[j].text.strip()))

file = open('./output/genieTOP100.txt','w')
file.write('{} 현재 Genie 뮤직 실시간 TOP 100\n'.format(df))
for i in range(100):
    file.write('{0:3d}위 {1} - {2}\n'.format(i+1,genie[i][0],genie[i][1]))
file.close()
print('genieTOP100.txt 쓰기 완료')

# text 파일에 저장된 데이터를 읽어서 화면에 출력한다
try:
    file = open('./output/genieTOP100.txt', 'r')
    lines = file.readlines()
    for line in lines:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print('디스크에 genieTOP100.txt 파일이 없습니다')