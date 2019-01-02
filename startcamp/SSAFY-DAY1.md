# DAY1(2018.12.17.월)

## 첫번째 시간

### 자기소개

- 전공
- 이름
- 프로그래밍 경험 여부

### 파이썬 코드작성

1. 크리스마스까지 남은 날짜 구하기

```python
from datetime import datetime, timedelta

n = datetime.today().strftime("%Y년 %m월 %d일")
d1 = datetime(2018, 12, 25)
d2 = datetime.now()
print("오늘의 날짜는",n,"입니다.")

print("크리스마스까지 {0}일 남았습니다.".format((d1-d2).days))
```



2. 로또(비복원추출)

```python
import random
numbers = list(range(1,46))
a = random.sample(numbers,6)
a.sort() #sort는 오름차순으로 정리해줌
print(a)
```



3. 저녁메뉴 고르기

```python
import random
menu = ["삼겹살","닭갈비","떡볶이","김밥","김치찌개","치킨"]
pick = random.choice(menu)
##어떻게 랜덤으로 뽑을까???
print(pick)
```



4. 미세먼지

```python
import requests
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=' + key + '&numOfRows=10&pageSize=10&pageNo=1&startPage=1&sidoName=%EA%B4%91%EC%A3%BC&ver=1.3'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
dong = soup('item')[7]
location = dong.stationName.text
time = dong.dataTime.text
dust = int(dong.pm10Value.text)

if 0<=dust<30:
  print("산책하러 나갑시다")
elif 30<=dust and dust<80:
  print("살만해요")
elif dust<150:
  print("마스크 쓰세요")
else:
  print("마스크 필수 꼭꼭 필수")

print("{0} 기준 {1}의 미세먼지 농도는 {2}입니다.".format(time,location,dust))
```



5. 저녁메뉴번호

```python
import random

# 1. menu 리스트를 만들어주세요.
menu = ['영암매력한우수완점','신전떡볶이 광주수완점','양동통닭','광주식당','회마켓','원조나주곰탕50년']

choice = random.choice(menu)
print(choice)

phonebook = {'영암매력한우수완점':'062-383-8118',
            '신전떡볶이 광주수완점':'062-956-2334',
             '양동통닭':'062-471-9277',
             '광주식당':'062-962-8284 ',
             '회마켓':'062-952-2026',
             '원조나주곰탕50년':'062-951-3255'
            }

print(phonebook['영암매력한우수완점'])
```



6. 코스피 url

```python
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

r = requests.get(url).text
soup = BeautifulSoup(r,'html.parser')
select = soup.select_one("#KOSPI_now")
print(select.text)
```



7. 안녕안녕안녕안녕안녕안녕

```python
greeting = [0,1,2,3,4,5]

for i in greeting:
  print("hello")
```



8. 미세먼지

```python
import requests
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=YNOYgnqfckC4PbaLGyN7HiFwbGe8MPhRN%2FjqmMufa7uqAffIl7D5fO%2BSh8zbRnzYfgo%2B4%2Bife1oj187l2mejMg%3D%3D&numOfRows=10&pageSize=10&pageNo=1&startPage=1&sidoName=%EA%B4%91%EC%A3%BC&ver=1.3'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
dong = soup('item')[7]
location = dong.stationName.text
time = dong.dataTime.text
dust = int(dong.pm10Value.text)

print("{0} 기준 {1}의 미세먼지 농도는 {2}입니다.".format(time,location,dust))
```



9. 안녕

```python
greeting="hello"

print(greeting)
print(greeting)
print(greeting)
print(greeting)
print(greeting)
```



### 오늘의 소감

크리스마스까지 남은 날짜를 구하는 것을 만들었다는 것이 매우 뿌듯하다!! 하하하하하하

컴퓨터는 참 신기하다.

내일도 빠샤!!!!!

오늘은 따라쓰느라 바빴지만 한학기 지나면 스스로 다 잘하겠지??



