from pywinauto.application import Application
import time
import time
import pygetwindow as gw
import pyautogui
import os
from pynput.keyboard import Controller, Key
from config.keyboard import keyboard


def open_xactimate():
    """Opens xactimate"""
    pyautogui.press("win")  # Press Windows key
    time.sleep(1)
    pyautogui.write("Xactimat") # Open Xactimate
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)

def get_xactimate_window():
    """Find xactimate window and bring it to the front"""
    time.sleep(2)  # Give time to open
    windows = gw.getWindowsWithTitle("Xactimate")
    if windows:
        win = windows[0]
        win.restore()
        win.activate()
        return win
    else:
        print("xactimate window not found!")
        return None


