import time
import pyautogui
time.sleep(4)
f = open('spam.txt')

for line in f:
    pyautogui.typewrite(line)
    pyautogui.press('enter')