import re #파이썬에서 정규표현식을 활용할 때 가장 자주 쓰이는 패키지 re 활용 문자열에서 숫자추출
import requests
import time # sleep() 1초시간지연

from bs4 import BeautifulSoup 

#get_text() 는 [리스트]에는 사용할 수 없다. 때문에 
#text_soup = BeautifulSoup(page.text,"html.parser") #text도 되나보다
#choo = text_soup.select('a') #웹페이지에서 a부분 찾는거
#check = soup.find_all(index) # index 찾는거

page = requests.get("http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=333")  #특정 URL에 접속하는 요청(Request) 객체를 생성
soup = BeautifulSoup(page.content, "html.parser")
arr = str(soup.td) #soup에 td 첫번째나오는것만 추출한것을 스트링으로 바꿔서 문자열 저장
result = re.sub(r'[^0-9]','',arr) # result에 숫자만 집어넣기
max = int(result)
print("-----절취선---------절취선---------절취선---------절취선----")

while True: #ctrl + c 누르면 끝난다고함 true일때
    page = requests.get("http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=333")  #특정 URL에 접속하는 요청(Request) 객체를 생성
    soup = BeautifulSoup(page.content, "html.parser")
    arr = str(soup.td) #soup에 td 첫번째나오는것만 추출한것을 스트링으로 바꿔서 문자열 저장
    result = re.sub(r'[^0-9]','',arr) # result에 숫자만 집어넣기

    if int(result) > max : #result가 문자형이니까 int로 바꿔주자
        print("새글나왔어")
        max = int(result)
    else :
        print("아직기다려봐")

    time.sleep(1) # 이것으로 1초간지연



