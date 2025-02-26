from config.keyboard import keyboard
from pynput.keyboard import  Key

def close_xactimate():
    """Closes xactimate"""
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.f4)
        keyboard.release(Key.f4)

