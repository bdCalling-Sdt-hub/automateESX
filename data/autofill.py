from re import search
from pywinauto.application import Application
import time
import autoit
from data import fillItems
from data.fillPriceList import fillPriceList
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
from utils.speak import speak
from utils.dropdown import select_dropdown_option
from utils.findAndClick import find_and_click, isExistImage
from data.autoFillQuantity import autoFillQuantity
from utils.end import close_xactimate
from data.fixingList import fixingList

window_title = autoit.win_get_title("")
print(f"Trying to access window with title: {window_title}")
if not window_title:
    print("Xactimate window not found.")


def typeDate(date):
    dateString = date.split(" ")
    pyautogui.write(dateString[0], interval=writeInterval)
    keyboard.press(Key.tab)
    pyautogui.write(f"{dateString[1]} ", interval=writeInterval)
    pyautogui.write(dateString[2], interval=writeInterval)
    keyboard.press(Key.tab)


policyTypes = ["Homeowner", "Commercial"]
writeInterval = 0.06


def write(data, interval):
    if data != None:
        pyautogui.write(data, interval=writeInterval)
    else:
        pass


def autoFill(data, text, exportESX):
    claim_number = data.get("claimDetails", {}).get("claimNumber", "")
    speak("Filling the form")
    time.sleep(1)
    pyautogui.hotkey("win", "up")
    time.sleep(1)
    if isExistImage("images/CLOSESIDE.png"):
        time.sleep(1)
        find_and_click("images/CLOSESIDE.png")
        time.sleep(1)
    # Client Information
    pyautogui.write(data.get("insured", {}).get("name", ""), interval=writeInterval)
    keyboard.press(Key.tab)
    pyautogui.write(data.get("insured", {}).get("email", ""), interval=writeInterval)
    # find_and_click("images/STREET.png")
    keyboard.press(Key.tab)
    keyboard.press(Key.tab)
    pyautogui.write(data.get("insured", {}).get("street", ""), interval=writeInterval)
    keyboard.press(Key.tab)
    pyautogui.write(data.get("insured", {}).get("city", ""), interval=writeInterval)
    keyboard.press(Key.tab)
    pyautogui.write(data.get("insured", {}).get("state", ""), interval=writeInterval)
    keyboard.press(Key.tab)
    pyautogui.write(data.get("insured", {}).get("zipCode", ""), interval=writeInterval)
    keyboard.press(Key.tab)
    time.sleep(1)
    keyboard.press(Key.tab)
    time.sleep(1)
    keyboard.press(Key.tab)
    time.sleep(1)
    keyboard.press(Key.tab)
    time.sleep(1)
    keyboard.press(Key.tab)
    time.sleep(1)
    keyboard.press(Key.tab)
    time.sleep(1)
    pyautogui.write(data.get("insured", {}).get("phone", ""), interval=writeInterval)
    keyboard.press(Key.tab)
    time.sleep(1)
    keyboard.press(Key.tab)
    time.sleep(1)
    keyboard.press(Key.tab)
    time.sleep(1)
    keyboard.press(Key.tab)
    time.sleep(1)
    typeDate(data.get("claimDetails", {}).get("dates", {}).get("loss", ""))
    typeDate(data.get("claimDetails", {}).get("dates", {}).get("entered", ""))
    typeDate(data.get("claimDetails", {}).get("dates", {}).get("received", ""))
    typeDate(data.get("claimDetails", {}).get("dates", {}).get("contacted", ""))
    typeDate(data.get("claimDetails", {}).get("dates", {}).get("inspected", ""))

    # Go to Loss and Coverage
    speak("Going to Loss and Coverage")
    time.sleep(2)
    location = pyautogui.locateOnScreen("images/CLAIMINFO.png", confidence=0.8)
    x,y=pyautogui.center(location)
    pyautogui.moveTo(x+100,y+25,duration=0.2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.write(f"{claim_number}", interval=writeInterval)
    keyboard.press(Key.tab)
    pyautogui.write(
        data.get("claimDetails", {}).get("policyNumber", ""), interval=writeInterval
    )
    keyboard.press(Key.tab)
    keyboard.press(Key.tab)
    find_and_click("images/TOL.png")
    pyautogui.write(
        data.get("claimDetails", {}).get("typeOfLoss", ""), interval=writeInterval
    )
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.press(Key.tab)
    keyboard.press(Key.tab)
    pyautogui.write("10349201", interval=writeInterval)
    find_and_click("images/AMOUNT.png")
    pyautogui.write(str(data.get("amount", 0)), interval=writeInterval)
    # going to parameters
    speak("Going to parameters")
    find_and_click("images/PARAMETERS.png")
    time.sleep(1)
    find_and_click("images/PRICELIST.png")
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(1)
    fillPriceList(data.get("claimDetails", {}).get("priceList", ""))
    time.sleep(3)
    keyboard.press(Key.down)
    time.sleep(1)
    keyboard.press(Key.down)
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(3)
    find_and_click("images/CHECKOUT_PRICELIST.png")
    time.sleep(1)
    keyboard.press(Key.space)
    time.sleep(2)
    keyboard.press(Key.enter)
    pyautogui.write(
        data.get("claimDetails", {}).get("priceList", ""), interval=writeInterval
    )
    keyboard.press(Key.enter)
    time.sleep(1)
    # adding estimates
    find_and_click("images/ESTIMATE.png")
    time.sleep(2)
    find_and_click("images/ESTIMATE_ITEM.png")
    time.sleep(2)
    estimationData = data.get("estimation", [])
    for section in estimationData:
        find_and_click("images/ADD.png")
        time.sleep(2)
        pyautogui.write(section.get("section", ""), interval=writeInterval)
        keyboard.press(Key.enter)
        time.sleep(2)
        data = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{getItemsPrompt(section.get('section', ''))} {text}",
                }
            ],
            model="gpt-4o",
        )
        data = (
            str(data.choices[0].message.content).replace("```", "").replace("json", "")
        )

        data = json.loads(data)
        print(data)
        for item in data.get("items", []):
            fillItems(item)
            time.sleep(2)

        autoFillQuantity(data.get("items", []))
        time.sleep(1)
    # closing the window
    time.sleep(5)
    with keyboard.pressed(Key.ctrl):
        keyboard.press("s")
        keyboard.release("s")
    time.sleep(2)
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.f4)
        keyboard.release(Key.f4)
    # Exporting the ESX
    if exportESX != False:
        speak("Form filled successfully now starting the export process")
        time.sleep(3)
        find_and_click("images/SEARCH.png")
        pyautogui.write(f"{claim_number}", interval=writeInterval)
        keyboard.press(Key.enter)
        time.sleep(2)
        find_and_click("images/SELECT.png")
        time.sleep(2)
        find_and_click("images/EXPORT.png")
        find_and_click("images/SAVEEXPORT.png")
        find_and_click("images/FINALEXPORT.png")
        time.sleep(2)
        keyboard.press(Key.enter)
        speak("Export process completed successfully")
