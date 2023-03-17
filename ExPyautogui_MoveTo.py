import pyautogui

for i in range(2):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(400, 100, duration=0.25)
    pyautogui.moveTo(400, 400, duration=0.25)
    pyautogui.moveTo(100, 400, duration=0.25)