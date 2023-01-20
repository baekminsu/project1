import pyautogui
import pyperclip
import time
#카카오 자동화 함수를 구현해보자

pyautogui.moveTo(1814,951) # 마우스 좌표이동
pyautogui.click() # 마우스클릭
#pyautogui.write('Hello sol test time') #키보드 입력 //한글로 이상하게나온다
pyperclip.copy("이건 카카오톡테스트") # 클립보드에 텍스트를 복사합니다.  //잘나온다
pyautogui.hotkey('ctrl', 'v') # 붙여넣기 (hotkey 설명은 아래에 있습니다.)
pyautogui.moveTo(1881,1018) #전송버튼이동
pyautogui.click() # 마우스클릭