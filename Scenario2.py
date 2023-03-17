import LibRPA as rpa
import keyboard

######################################################
# 1. 縮小目前 Pychram by Python Project Name - PythonRPA
# 2. 將其他程式放大視窗 LOOP HERO
# 3. 進入無窮迴圈，按下 CTRL+C 離開迴轉
# 4. 放大視窗 PythonRPA
#
# 相關程式來自 LibRPA Program
######################################################

#Pycharm PROJECT PythonRPA 縮到最小
rpa.minimize_window("PythonRPA")
rpa.maximize_window("LOOP HERO")

while True:
    try:
        if keyboard.is_pressed("ctrl+c"):
            print("KeyboardInterrupt")
            break
    except KeyboardInterrupt:
        print("KeyboardInterrupt")

rpa.maximize_window("PythonRPA")

print("finished")