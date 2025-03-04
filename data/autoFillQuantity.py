import time

import pyautogui

from data.fixingList import fixingList
from utils.findAndClick import find_and_click, isExistImage


def click(x, y):
    pyautogui.moveTo(x, y, duration=0.2)
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
    locations = list(
        pyautogui.locateAllOnScreen("images/QUANTITYCLICK.png", confidence=0.8)
    )
    x1, y1 = pyautogui.center(locations[0])
    click(x1, y1)
    print(f"x1: {x1}, y1: {y1}")
    locations2 = list(
        pyautogui.locateAllOnScreen("images/DESCRIPTION.png", confidence=0.8)
    )
    x2, y2 = pyautogui.center(locations2[0])
    click(x2, y2)
    print(f"x2: {x2}, y2: {y2}")
    pyautogui.moveTo(x2, y2 + 100)
    for i in range(len(items)):
        pyautogui.scroll(50)
