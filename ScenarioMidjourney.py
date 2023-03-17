import LibRPA as rpa
import pyperclip
import keyboard
import pyautogui
import time

def main():
    # Pycharm PROJECT PythonRPA 縮到最小
    rpa.minimize_window("PythonRPA")
    rpa.maximize_window("DISCORD")

    g_confidence = 0.8
    g_duration = 0.4
    g_midjourney_text = "images/midjourney_text.png"
    g_midjourney_complete = "images/midjourney_complete.png"
    g_midjourney_complete2 = "images/midjourney_complete2.png"

    # 開啟檔案
    with open(r"C:\temp\ai_prompt.txt", "r") as file:
        # 逐行讀取檔案內容並顯示
        for line in file:
            #攔截鍵盤如有按 ctrl+c 則離開迴圈
            try:
                if keyboard.is_pressed("ctrl+c"):
                    print("KeyboardInterrupt")
                    break
            except KeyboardInterrupt:
                print("KeyboardInterrupt")

            #將變數值記錄在記憶體
            print(line.strip())

            l_found, l_pos = rpa.pic_exist_pos(g_midjourney_text, g_confidence)
            if l_found == True:
                pyautogui.moveTo(l_pos[0] + 150, l_pos[1] + 20, duration=g_duration)
                pyautogui.click(l_pos[0] + 150, l_pos[1] + 20)

                pyperclip.copy(line.strip())
                pyautogui.hotkey('ctrl', 'v')

                pyautogui.press('enter')
                pyautogui.press('enter')

                time.sleep(2)

                while True:
                    # 攔截鍵盤如有按 ctrl+c 則離開迴圈
                    try:
                        if keyboard.is_pressed("ctrl+c"):
                            print("KeyboardInterrupt")
                            break
                    except KeyboardInterrupt:
                        print("KeyboardInterrupt")
                    l_found, l_pos = rpa.pic_exist_pos(g_midjourney_complete, g_confidence)
                    if l_found == True:
                        print("Find Complete 1")
                        break
                    else:
                        print("Wait Complete 1")

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
