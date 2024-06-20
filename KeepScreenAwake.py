import time
import pyautogui

while True:
    print("the Mouse start moving")
    pyautogui.move(0, 1)   # Move mouse by 1 pixel
    pyautogui.move(0, -1)  # Move mouse back
    print("Start waiting for 1 min")
    time.sleep(60)
    print("Count down is over")
