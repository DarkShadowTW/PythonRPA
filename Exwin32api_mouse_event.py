#沒有慢慢移動的感覺

# Import modules
import win32api, win32con

# Set target position
tx, ty = 0, 0

# Mouse move event
win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(tx/win32api.GetSystemMetrics(0)*65535), int(ty/win32api.GetSystemMetrics(1)*65535) ,0 ,0)