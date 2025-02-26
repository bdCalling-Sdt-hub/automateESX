from pywinauto.application import Application
import time
import time
import pygetwindow as gw
import pyautogui
import os
from pynput.keyboard import Controller, Key
from utils.startup import open_xactimate, get_xactimate_window
from config.keyboard import keyboard
from utils.end import close_xactimate
from utils.speak import speak

def new_project():
    time.sleep(5)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('n')
        keyboard.release('n')
        speak("New Project Form Opened")
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)
    keyboard.press(Key.esc)
    time.sleep(2)
    speak("New Project Created")
    time.sleep(2)
        

