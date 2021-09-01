import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings(action='ignore')
import datetime
df=datetime.datetime.now()

targetSite='https://www.melon.com/chart/index.htm'
header = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
request =requests.get(targetSite, headers=header)
html=request.text
soup = BeautifulSoup(html,'html.parser')
# 406(허용되지 않음): 요청한 페이지가 요청한 콘텐츠 특성으로 응답할 수 없다
# print(request)

# print(soup)
titles = soup.findAll('div', {'class':'ellipsis rank01'})
# ellipsis rank02

artists = soup.findAll('span', {'class':'checkEllipsis'})
# for artist in artists:
#     print(artist.text.split('\n')[0])
# for i in range(100):
#     artist = artists[i].text.strip().split('\n')[0]
#     title = titles[i].text.strip()
#     print('{0:3d}위 {1} - {2}'.format(i+1,artist,title))

file = open('./output/melonTOP100.txt','w')
file.write('{} 현재 Melon 뮤직 실시간 TOP 100\n'.format(df))
for i in range(100):
    artist = artists[i].text.strip().split('\n')[0]
    title = titles[i].text.strip()
    file.write('{0:3d}위 {1} - {2}\n'.format(i+1,artist,title))
file.close()
print('melonTOP100.txt 쓰기 완료')

# text 파일에 저장된 데이터를 읽어서 화면에 출력한다
try:
    file = open('./output/melonTOP100.txt', 'r')
    lines = file.readlines()
    for line in lines:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print('디스크에 melonTOP100.txt 파일이 없습니다')