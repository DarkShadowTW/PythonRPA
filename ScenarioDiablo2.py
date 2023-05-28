import LibRPA as rpa
import pyperclip
import keyboard
import pyautogui
import time

def main():
    # Pycharm PROJECT PythonRPA 縮到最小
    rpa.minimize_window("PythonRPA")
    rpa.maximize_window("Diablo II")

    #全域變數
    g_confidence = 0.8          #要找的圖片信心度符合呈度即算找到
    g_duration = 0.2            #滑鼠移動的時間長度
    g_mousebutton_duration = 0.1      #滑鼠按下鍵的時間長度

    g_buy_homescroll_city1 = "images_diablo2/01_city_buy_home_scrolling.png" #老婆婆的建築物

    while True:
        # 攔截鍵盤如有按 ctrl+c 則離開迴圈
        try:
            if keyboard.is_pressed("ctrl+c"):
                print("KeyboardInterrupt")
                break
        except KeyboardInterrupt:
            print("KeyboardInterrupt")

        #判斷圖片是否已產生完成的條件 - 1 與下方 2 是 or 條件
        l_found, l_pos = rpa.pic_exist_pos(g_buy_homescroll_city1, g_confidence)
        if (l_found == True and l_pos[0] < 1000):
            pyautogui.moveTo(l_pos[0], l_pos[1], duration=g_duration)
            pyautogui.mouseDown(button='left', duration=g_mousebutton_duration)
            print("found")
        else:
            pyautogui.mouseUp(button='left')
            print("not found")

    rpa.maximize_window("PythonRPA")

    print("END")

if __name__ == '__main__':
    main()
