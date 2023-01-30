'''
개선해야할것들
1.이용자에게 i번째 확인했다고 출력
2.컴퓨터 프로그램측에서 카톡으로 보내기하기 마우스키보드 제어가아닌
3. 새글 알람이아닌 "세종 스테이 " 키워드가 있을때 알려주기
4. 수면중 카톡보내기였는데 꺠어있을때는 소리로 울릴것

4버전에서는 소리추가를 넣을것 카톡보내기 삭제예정(임시)
 '''
import re # 파이썬에서 정규표현식을 활용할 때 가장 자주 쓰이는 패키지 re 활용 문자열에서 숫자추출
import requests
import time # sleep() 1초시간지연
import pyautogui
import pyperclip # gui 한글나오게하려고 copy 기능과 붙여넣기 기능 첨가
import time
import winsound as sd  # 사운드추가

from bs4 import BeautifulSoup 

#get_text() 는 [리스트]에는 사용할 수 없다. 때문에 
#text_soup = BeautifulSoup(page.text,"html.parser") #text도 되나보다
#choo = text_soup.select('a') #웹페이지에서 a부분 찾는거
#check = soup.find_all(index) # index 찾는거

def beepsound(): # 사운드 함수
    fr = 2000
    du = 1000
    sd.Beep(fr,du)

page = requests.get("http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=333")  #특정 URL에 접속하는 요청(Request) 객체를 생성
soup = BeautifulSoup(page.content, "html.parser")
arr = str(soup.td) #soup에 td 첫번째나오는것만 추출한것을 스트링으로 바꿔서 문자열 저장
result = re.sub(r'[^0-9]','',arr) # result에 숫자만 집어넣기
max = int(result)
count = 0
i = 0
print("----시작---------시작---------시작---------시작----")

while True: #ctrl + c 누르면 끝난다고함 true일때

    page = requests.get("http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=333")  #특정 URL에 접속하는 요청(Request) 객체를 생성
    soup = BeautifulSoup(page.content, "html.parser")
    arr = str(soup.td) #soup에 td 첫번째나오는것만 추출한것을 스트링으로 바꿔서 문자열 저장
    result = re.sub(r'[^0-9]','',arr) # result에 숫자만 집어넣기

    if int(result) > max : #result가 문자형이니까 int로 바꿔주자
        while i < 10 :
            beepsound()
            beepsound()
            max = int(result)
            i = i +1
        i = 0
    else :
        print("%d 번째 확인중" %(count))
        print("%d max는 이값이였음"%(max))

    count = count +1
    time.sleep(1200) # 이것으로 30초간지연
    



