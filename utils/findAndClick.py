import pyautogui
import cv2
import numpy as np
import pytesseract
import time
import pyscreeze

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def find_and_click(image_path, confidence=0.8, timeout=10, rightClick=False):

    """
    Finds an image on the screen and clicks on it.
    
    :param image_path: Path to the reference image.
    :param confidence: Matching confidence level (0.8 = 80% match).
    :param timeout: Time (seconds) to keep searching before giving up.
    """
    try:
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            
            if location:
                x, y = pyautogui.center(location)  # Get center coordinates
                if rightClick:
                    pyautogui.rightClick(x, y, duration=1)  # Click on the found image
                else:
                    pyautogui.click(x, y, duration=1)  # Click on the found image
                return True
        time.sleep(0.5)  # Wait a bit before retrying
        return False
    except (pyautogui.ImageNotFoundException, pyscreeze.ImageNotFoundException):
        return False
def isExistImage(image_path, confidence=0.8):
    """
    Checks if an image is on the screen with a given confidence level.
    
    :param image_path: Path to the image to check.
    :param confidence: Matching confidence level (0.8 = 80% match).
    :return: True if the image is found, False otherwise.
    """
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        return location is not None
    except (pyautogui.ImageNotFoundException, pyscreeze.ImageNotFoundException):
        return False