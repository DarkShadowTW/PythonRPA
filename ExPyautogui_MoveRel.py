import pyautogui

for i in range(2):
    pyautogui.moveRel(400, 0, duration=0.25)
    pyautogui.moveRel(0, 400, duration=0.25)
    pyautogui.moveRel(-400, 0, duration=0.25)
    pyautogui.moveRel(0, -400, duration=0.25)
