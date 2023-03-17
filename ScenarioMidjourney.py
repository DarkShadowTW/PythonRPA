import LibRPA as rpa
import pyperclip
import keyboard
import pyautogui
import time

def main():
    # Pycharm PROJECT PythonRPA 縮到最小
    rpa.minimize_window("PythonRPA")
    rpa.maximize_window("DISCORD")

    #全域變數
    g_confidence = 0.8          #要找的圖片信心度符合呈度即算找到
    g_duration = 0.4            #滑鼠移動的時間長度
    g_midjourney_text = "images/midjourney_text.png"             #找尋目前 Discord 文字輸入的位置
    g_midjourney_complete = "images/midjourney_complete.png"     #當看到什麼表示要貼下一則 - 1 or
    g_midjourney_complete2 = "images/midjourney_complete2.png"   #當看到什麼表示要貼下一則 - 2

    # 開啟檔案
    with open(r"C:\temp\ai_prompt.txt", "r") as file:
        # 逐行讀取檔案內容並顯示
        for line in file:
            #攔截鍵盤如有按 shift+alt+c 則離開迴圈
            try:
                if keyboard.is_pressed("shift+alt+c"):
                    print("KeyboardInterrupt")
                    break
            except KeyboardInterrupt:
                print("KeyboardInterrupt")

            #將變數值記錄在記憶體
            print(line.strip())

            #看畫面上是否有找到指定的圖片
            l_found, l_pos = rpa.pic_exist_pos(g_midjourney_text, g_confidence)
            if l_found == True:
                #移動並按下 Click
                pyautogui.moveTo(l_pos[0] + 150, l_pos[1] + 20, duration=g_duration)
                pyautogui.click(l_pos[0] + 150, l_pos[1] + 20)

                #把提辭放到記憶體並貼到文字
                pyperclip.copy(line.strip())
                pyautogui.hotkey('ctrl', 'v')

                #按兩下ENTER讓提辭傳出 (1. 輸入後轉換成 /img... 的輸入畫面, 2. 傳出)
                pyautogui.press('enter')
                pyautogui.press('enter')

                #等待 2 秒
                time.sleep(2)

                #直到有人按下 shift+alt+c 結束
                while True:
                    # 攔截鍵盤如有按 ctrl+c 則離開迴圈
                    try:
                        if keyboard.is_pressed("shift+alt+c"):
                            print("KeyboardInterrupt")
                            break
                    except KeyboardInterrupt:
                        print("KeyboardInterrupt")

                    #判斷圖片是否已產生完成的條件 - 1 與下方 2 是 or 條件
                    l_found, l_pos = rpa.pic_exist_pos(g_midjourney_complete, g_confidence)
                    if l_found == True:
                        print("Find Complete 1")
                        break
                    else:
                        print("Wait Complete 1")

                    # 判斷圖片是否已產生完成的條件 - 2
                    l_found, l_pos = rpa.pic_exist_pos(g_midjourney_complete2, g_confidence)
                    if l_found == True:
                        print("Find Complete 2")
                        break
                    else:
                        print("Wait Complete 2")

    rpa.maximize_window("PythonRPA")

    print("END")

if __name__ == '__main__':
    main()
