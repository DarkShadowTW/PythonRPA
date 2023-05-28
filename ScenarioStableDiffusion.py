import LibRPA as rpa
import pyperclip
import keyboard
import pyautogui
import time


def main():
    # Pycharm PROJECT PythonRPA 縮到最小
    rpa.minimize_window("PythonRPA")
    rpa.maximize_window("Edge")

    #全域變數
    g_confidence = 0.8          #要找的圖片信心度符合呈度即算找到
    g_duration = 0.4            #滑鼠移動的時間長度



    rpa.maximize_window("PythonRPA")

    print("END")


if __name__ == '__main__':
    main()
