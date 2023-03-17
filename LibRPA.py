#import win32api
import win32gui
import win32con
import pyautogui

#===============================================================
#視窗縮到最小
#===============================================================
def callback_min(hwnd, title):
    if title in win32gui.GetWindowText(hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
        return False
    return True

def minimize_window(title):
    try:
        win32gui.EnumWindows(callback_min, title)
    except:
        print("win32gui.EnumWindows(callback, title) Get Exception")

def callback_max(hwnd, title):
    if title in win32gui.GetWindowText(hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        return False
    return True

def maximize_window(title):
    try:
        win32gui.EnumWindows(callback_max, title)
    except:
        print("win32gui.EnumWindows(callback, title) Get Exception")

#===============================================================
#判斷圖片是否存在
#===============================================================
def pic_exist(p_img_path, p_confidence):
    l_position = pyautogui.locateOnScreen(p_img_path, confidence=p_confidence)
    if l_position is not None:
        return True
    else:
        return False

#===============================================================
#判斷圖片是否存在並回傳位置
#===============================================================
def pic_exist_pos(p_img_path, p_confidence):
    l_position = pyautogui.locateOnScreen(p_img_path, confidence=p_confidence)
    if l_position is not None:
        return True, l_position
    else:
        return False, None

#===============================================================
#移動滑鼠
#===============================================================
def pic_moveto(p_img_path, p_confidence, p_duration):
    l_position = pic_exist_pos(p_img_path, p_confidence=p_confidence)[1]
    if l_position is not None:
        pyautogui.moveTo(l_position[0], l_position[1], duration=p_duration)

#===============================================================
#點擊滑鼠
#===============================================================
def pic_click(p_img_path, p_confidence, p_click_time):
    l_position = pic_exist_pos(p_img_path, p_confidence=p_confidence)[1]
    if l_position is not None:
        try:
            if p_click_time == 1:
                pyautogui.Click(l_position)
            else:
                pyautogui.doubleClick(l_position)
        except:
            print("doubleClick Failed", p_img_path)