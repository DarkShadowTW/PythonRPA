import LibRPA as rpa
import keyboard

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