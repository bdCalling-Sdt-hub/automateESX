
import time

import pyautogui

from data.fixingList import fixingList
from utils.findAndClick import find_and_click, isExistImage


def click(x,y):
    pyautogui.moveTo(x,y,duration=0.2)
    pyautogui.click()
# time.sleep(10)
# y=650
# for i in range(10):
#     click(1080, y)
#     pyautogui.hotkey('ctrl', 'a')
#     pyautogui.press('backspace')
#     pyautogui.write("123", interval=0.05)
#     y = y+25
# time.sleep(10)


def autoFillQuantity(items):
    # fixingList(items)
    time.sleep(1)
    locations = list(pyautogui.locateAllOnScreen("images/QUANTITYCLICK.png", confidence=0.8))   
    x, y = pyautogui.center(locations[0]) 
    index = 0
    time.sleep(1)
    # if(len(items) > 14):
    #     pyautogui.scroll(-200)
    y = y+25
    time.sleep(1)
    for item in items:
        try:
            click(x, y)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.write(str(item.get('quantity', 0)), interval=0.05)
            y = y+25
            index = index +1
            if(len(items) > 13):
                pyautogui.scroll(10)
            time.sleep(2)
        except Exception as e:
            print(e)