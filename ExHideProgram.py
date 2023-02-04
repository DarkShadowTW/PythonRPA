import win32api
import win32gui
import win32con

def callback(hwnd, hwnds):
    if "PythonRPA" in win32gui.GetWindowText(hwnd):
        print("IN")
        hwnds.append(hwnd)
        return False
    return True

def minimize_window(title):
    hwnds = []
    try:
        win32gui.EnumWindows(callback, hwnds)
    except:
        print("EXCEPTION")
    for hwnd in hwnds:
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

minimize_window("PyCharm")