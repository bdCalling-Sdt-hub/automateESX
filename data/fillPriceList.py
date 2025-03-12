from re import search
from numpy import isneginf
from pywinauto.application import Application
import time
import autoit
from data import fillItems
from data.getESX import getESX
import pygetwindow as gw
import pyautogui
from data.fillItems import fillItems
from config.allItemPrompt import getItemsPrompt
import os
from config.openAiClient import client
import json
import pyperclip
from pynput.keyboard import Controller, Key
from config.keyboard import keyboard
from utils import findAndClick
from utils.speak import speak
from utils.dropdown import select_dropdown_option
from utils.findAndClick import find_and_click, isExistImage
from data.autoFillQuantity import autoFillQuantity
from utils.end import close_xactimate
from datetime import datetime


def get_adjusted_date(price_list):
    """
    Takes a price_list string (format like 'PRICE_JAN25' or 'PRICE_AUG15') and returns
    a properly formatted date string with the correct year based on current date.

    Returns date in format 'M/D/YYYY' (e.g., '1/25/2025')
    """
    now = datetime.now()
    current_month = now.month
    current_year = now.year

    # Parse month and day from price_list string
    month_str = price_list.split("_")[1][:3].upper()
    day = int(price_list.split("_")[1][3:])

    # Map month abbreviations to numbers
    month_dict = {
        "JAN": 1,
        "FEB": 2,
        "MAR": 3,
        "APR": 4,
        "MAY": 5,
        "JUN": 6,
        "JUL": 7,
        "AUG": 8,
        "SEP": 9,
        "OCT": 10,
        "NOV": 11,
        "DEC": 12,
    }

    month = month_dict.get(month_str, 1)

    # Determine year based on whether the date has passed this year
    if (month < current_month) or (month == current_month and day < now.day):
        year = current_year
    else:
        year = current_year - 1

    # Format the date string
    if day < 10:
        day = f"0{day}"
    return f"{month}/{day}/{year}"


def fillPriceList(priceList):
    time.sleep(3)
    pyautogui.write(str(priceList), interval=0.06)
    time.sleep(3)
    noPriceList = isExistImage("images/NOPRICELISTPIC.png")
    time.sleep(3)
    if noPriceList:
        try:
            pyautogui.hotkey("ctrl", "a")
            time.sleep(1)
            pyautogui.press("backspace")

            time.sleep(2)
            # print(priceList)
            # find_and_click("images/REQUESTPRICELIST.png")
            # time.sleep(2)
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.press("tab")
            time.sleep(1)
            thisDate = get_adjusted_date(priceList)
            pyautogui.write(thisDate, interval=0.06)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(3)
            find_and_click("images/DOWNLOAD.png")
            time.sleep(10)
            find_and_click("images/NEXT.png")
            time.sleep(5)
        except Exception as e:
            print(e)
    else:
        try:
            time.sleep(5)
            find_and_click("images/NEXT.png")
            time.sleep(3)
        except Exception as e:
            print(e)
