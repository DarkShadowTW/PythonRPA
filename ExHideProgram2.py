import win32api
import win32gui
import win32con

def callback(hwnd, title):
    if title in win32gui.GetWindowText(hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
        return False
    return True

def minimize_window(title):
    try:
        win32gui.EnumWindows(callback, title)
    except:
        print("win32gui.EnumWindows(callback, title) Get Exception")

minimize_window("PythonRPA")