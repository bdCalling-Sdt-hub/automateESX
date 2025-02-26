from pywinauto.application import Application
import time
import autoit

import pygetwindow as gw
import pyautogui
import os
from pynput.keyboard import Controller, Key
from config.keyboard import keyboard
from utils.speak import speak
from utils.dropdown import select_dropdown_option
from utils.findAndClick import find_and_click


def getESX(uniqueIdentifier):
    find_and_click("images/SEARCH.png")
    pyautogui.write(f"{uniqueIdentifier}")
    find_and_click("images/SELECT.png")
    find_and_click("images/EXPORT.png")
    find_and_click("images/SAVEEXPORT.png")
    find_and_click("images/FINALEXPORT.png")
