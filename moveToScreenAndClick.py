import pyautogui
import time
import pyperclip
from utils.findAndClick import find_and_click

def click(x, y):
    """Moves the mouse to (x, y) and clicks."""
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.click()
time.sleep(10)

start_x = 724
start_y = 650

row_offset = 25

lastCopiedText = ""

time.sleep(1)
for index in range(13):
        click(start_x, start_y)
        time.sleep(1)  
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1) 
        pyautogui.rightClick()
        time.sleep(1) 
        find_and_click("images/COPY.png")
        time.sleep(1) 
        copied_value = pyperclip.paste()
        if(copied_value == lastCopiedText and lastCopiedText != ""):
            time.sleep(1)
            pyautogui.moveTo(int(start_x)-20, int(start_y)-5)
            pyautogui.rightClick()
            time.sleep(1)
            find_and_click("images/DELETE.png")
        lastCopiedText = copied_value
        print(f"Row {index + 1} Copied Text: {copied_value}")
        start_y += row_offset
        time.sleep(1)
    

