# DAY2(2018.12.18.화)

## 웹 크롤링

### GIT FOR WINDOWS 설치

- Unix tools 체크하고 설치하기
- Git Bash 실행



### GIT BASH 명령어

- pwd : 현재의 위치(디렉토리)를 나타냄
- touch a.txt : a.txt 라는 파일 생성
- clear : 모두 지우기
- python -V : 파이썬의 버전 보여주기
- cd 파일명 : 현재 디렉토리 내 파일로 이동
- python python.py : 파일 실행
- pip install requests : requests에 대한 모듈 설치
- pip install bs4



### PYTHON 설치

- PYTHON DOWNLOAD - ALL REALEASE - WEB BASED INSTALLER
- 3.6.7 버전으로 설치
- 설치과정에서 환경변수 등록 누르고 설치하기



### VS CODE 설치

- 실행 후 ctrl+shift+x 에서 korea language pack 설치 후 restart
- ctrl+shift+p 에서 shell 검색 후 Git Bash로 설정하기
- ctrl+`를 누르면 터미널이 나와요!



### Webbrowser

- webbrowser.open()
- webbrowser.open_new() : 새창으로 열기
- webbrowser.open_new_tap() : 새탭으로 열기



```python
import webbrowser

url = "https://google.com"
url = "https://samsung.com"
url = "https://www.google.com/search?&q=ssafy"
webbrowser.open(url)
```



```python
import webbrowser

q_list = ["bts","아이유","블랙핑크","위너"]

url = "https://www.google.com/search?&q="

for q in q_list:
    webbrowser.open(url+q)
```

#q  = "여기에 검색어 쓰기"



```python
import requests

url = "https://google.com"
res = requests.get(url).status_code
print(res)
```



#requests.get(url) 의 결과 : 

​	$ python crawling.py
​	<Response [200]>

#requests.get(url).status_code 의 결과 :

​	$ python crawling.py
​	200







### 실습

- 크롬에서 원하는 정보 가져오기 (실시간 검색어 가져오기)
  - 동성제약 - 오른쪽버튼에서 검색 - 오른쪽버튼에서 copy - copy selector
- 다음 실시간 검색어 1위 출력

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net/"
res = requests.get(url).text
#res = requests.get(url).status_code

soup = BeautifulSoup(res,'html.parser')
pick = soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li:nth-of-type(1) > div > div:nth-of-type(1) > span.txt_issue > a')
print(pick)
```

​	#bs4 에서 child 라는 명령을 인식 못하므로 같은 의미인 of-type 으로 바꿔줌

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net/"
res = requests.get(url).text
#res = requests.get(url).status_code

soup = BeautifulSoup(res,'html.parser')
pick = soup.select_one('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li:nth-of-type(1) > div > div:nth-of-type(1) > span.txt_issue > a')
print(pick.text)
```

​	#select_one으로 하면 "조재범" 이렇게만 나온다!!

​	#select : 문서 안에 있는 특정 내용을 뽑아줘. 모든 요소를 리스트로 반환

​	#select_one : 객체 하나를 반환



- 다음 실시간 검색어 전체 출력

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net/"
res = requests.get(url).text
#res = requests.get(url).status_code

soup = BeautifulSoup(res,'html.parser')
pick = soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li > div > div:nth-of-type(1) > span.txt_issue > a')
print(pick)
```

​	#위에꺼랑 차이점은 li 뒤에있는거를 지웠느냐 안지웠느냐!!

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net/"
res = requests.get(url).text
#res = requests.get(url).status_code

soup = BeautifulSoup(res,'html.parser')
picks = soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li > div > div:nth-of-type(1) > span.txt_issue > a')
for p in picks:
    print(p.text)

#print(pick)
```

​	#이렇게하면 1위부터 10위까지 검색어만 딱 뜬다!!



- 비트코인 정보 불러오기

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.bithumb.com/"
res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')
coins = soup.select('tbody.coin_list tr')
for coin in coins:
    print(coin.select_one("td:nth-of-type(1) a strong").text)
    print(coin.select_one("td:nth-of-type(2) strong").text)
    #print(coin)
#print(coin)
```





- 멜론 차트 불러오기

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}
response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response,'html.parser')

music_table = soup.select("table tr.lst50")

for music in music_table:
    number = music.select_one("span.rank").text
    title = music.select_one("div.wrap_song_info a").text
    print(number +"위 : "+ title)
```



- 파일명 바꾸기

  기존파일명 앞에 있는 SAMSUNG을 SSAFY 로 바꾸기

```python
import os

os.chdir(r'C:\Users\student\change\SSAFY지원자')

for filename in os.listdir("."):
    data = filename.replace('SAMSUNG','SSAFY')
    os.rename(filename,data)
    #os.rename(filename,"SAMSUNG"+filename)
```



ctrl+/ 누르면 해당 줄이 주석처리 됩니다.



git init : 

ls : 현재 폴더

ls -a : 모든 폴더 

. : 현재폴더

.. : 상위폴더

폴더앞에. : 비밀폴더



### GitHub 등록하기



