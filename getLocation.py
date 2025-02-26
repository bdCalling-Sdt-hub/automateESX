import pyautogui
import time

# Give you 5 seconds to move your mouse to the desired location
print("Move your mouse to the target location in 5 seconds...")
time.sleep(10)

# Get and print the current mouse position
x, y = pyautogui.position()
print(f"Mouse position: x={x}, y={y}")