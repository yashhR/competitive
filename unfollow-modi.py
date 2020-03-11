import time
import pyautogui


ask = input("Do you want to unfollow Modi?")
if ask.lower() == "yes" or ask.lower() == "y":
    pyautogui.moveTo(209, 647, duration=1)
    pyautogui.click()
    pyautogui.moveTo(560, 647, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(686, 289, duration=0.5)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(1177, 480, duration=0.5)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(1062, 661, duration=0.5)
    pyautogui.click()
else:
    print("Fuck off!")
