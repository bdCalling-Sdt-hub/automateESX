import pyautogui
import cv2
import numpy as np
import pytesseract
import time

# Set Tesseract path (Modify this if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def find_and_click_text(target_text, action="click", type_text=None):
    """Finds a button or input field by visible text and interacts with it.

    Args:
        target_text (str): The text to search for on the screen.
        action (str): "click" to press a button, "type" to enter text.
        type_text (str, optional): The text to enter if action is "type".
    """
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    
    # Convert to grayscale
    gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    
    # OCR to detect text
    data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
    
    for i in range(len(data["text"])):
        if target_text.lower() in data["text"][i].lower():
            x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
            center_x, center_y = x + w // 2, y + h // 2

            # Move and click
            pyautogui.moveTo(center_x, center_y, duration=0.2)
            pyautogui.click()
            time.sleep(0.5)

            # If typing is needed
            if action == "type" and type_text:
                pyautogui.write(type_text, interval=0.05)
                pyautogui.press("enter")
            
            return True  # Successfully found and clicked

    print(f"Text '{target_text}' not found on screen.")
    return False  # Text not found

