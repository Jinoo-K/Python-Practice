# pip install pyautogui
# pip install pyperclip
# pip install schedule

import pyautogui
import pyperclip
import time
import threading
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def send_message():
    threading.Timer(10, send_message).start()       # 10초 후에 함수 실행
    
    picPosition = pyautogui.locateOnScreen("pic1.png")
    print(picPosition)

    if picPosition is None : 
        picPosition = pyautogui.locateOnScreen("pic2.png")
        
    if picPosition is None :
        picPosition = pyautogui.locateOnScreen("pic3.png")
        print(picPosition)
        
    clickPosition = pyautogui.center(picPosition)
    pyautogui.doubleClick(clickPosition)

    pyperclip.copy("이 메세지는 자동으로 보내는 메세지입니다!!!")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2.0)

    pyautogui.write(["Enter"])
    time.sleep(2.0)

    pyautogui.write(["Escape"])
    time.sleep(1.0)
    
send_message()