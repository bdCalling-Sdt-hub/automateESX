from re import search
from openai import Client
from pywinauto.application import Application
import time
import autoit
from data.getESX import getESX
import pygetwindow as gw
import pyautogui
import os
import pyperclip
from pynput.keyboard import Controller, Key
from config.keyboard import keyboard
from utils.speak import speak
from utils.dropdown import select_dropdown_option
from utils.findAndClick import find_and_click, isExistImage
from utils.end import close_xactimate
def checkAndWrite(text):
    time.sleep(1)
    writeInterval = 0.05
    if(text != '') or text != None or text != 'N/A' or text != 'None':
        pyautogui.write(str(text), interval=writeInterval)
def tab():
    time.sleep(1)
    keyboard.press(Key.tab)
def enter():
    time.sleep(1)
    keyboard.press(Key.enter)
def selectAllAndClean():
    time.sleep(1)
    with keyboard.pressed(Key.ctrl):    
        keyboard.press('a')
        keyboard.release('a')
    keyboard.press(Key.backspace)

def fillItems(item):
    try:
       
        if(isExistImage("images/DUPLICATED.png")):
            find_and_click("images/DUPLIYES.png")
        else:
            time.sleep(1)
            find_and_click("images/SEARCHITEM.png")
            pyautogui.write(item.get('desc', ''), interval=0.06)
            time.sleep(2)
            keyboard.press(Key.down)
            time.sleep(1)
            enter()
            time.sleep(2)
        
        
       
    except Exception as e:
        print(e)
    
