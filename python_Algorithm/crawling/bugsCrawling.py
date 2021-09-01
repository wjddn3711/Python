import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings(action='ignore')
import datetime
df=datetime.datetime.now()

targetSite='https://music.bugs.co.kr/chart?wl_ref=M_left_02_01'
request =requests.get(targetSite)
html=request.text
soup = BeautifulSoup(html,'html.parser')

# 노래제목 크롤링
titles = soup.findAll('p', {'class':'title'})

# for i in range(len(titles)):
    # print('{0:3d}위 {1}'.format(i+1,titles[i].text.strip()))
    # print('{0:3d}위 {1}'.format(i+1,titles[i].text.split('\n')[1]))
    # print(titles[i].text.split('\n')[1])

artists = soup.findAll('p', {'class':'artist'})
# for i in range(len(artists)):
#     print('{0:3d}위 {1:50s}'.format(i + 1, titles[i].text.strip()))
#     print('{0:s}'.format(artists[i].text.strip().split('\n')[0]))

# print(df)
# for i in range(100):
#     artist = artists[i].text.strip().split('\n')[0]
#     title = titles[i].text.strip()
#     print('{0:3d}위 {1} - {2}'.format(i+1,artist,title))

# 크롤링한 결과를 텍스트 파일로 저장한다
file = open('./output/bugsTOP100.txt','w')
file.write('{} 현재 Bugs 뮤직 실시간 TOP 100\n'.format(df))
for i in range(100):
    artist = artists[i].text.strip().split('\n')[0]
    title = titles[i].text.strip()
    file.write('{0:3d}위 {1} - {2}\n'.format(i+1,artist,title))
file.close()
print('bugsTOP100.txt 쓰기 완료')

# text 파일에 저장된 데이터를 읽어서 화면에 출력한다
try:
    file = open('./output/bugsTOP100.txt', 'r')
    lines = file.readlines()
    for line in lines:
        print(line.strip())
    file.close()
except FileNotFoundError:

    print('디스크에 bugsTOP100.txt 파일이 없습니다')