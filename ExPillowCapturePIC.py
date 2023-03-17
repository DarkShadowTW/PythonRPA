from PIL import ImageGrab

x = 100
y = 100

# 擷取區域的左上角座標
left = x - 0
top = y - 100

# 擷取區域的右下角座標
right = left + 50
bottom = top + 70

# 擷取圖片
im = ImageGrab.grab(bbox=(left, top, right, bottom))

# 儲存圖片
im.save('temp/screenshot.png', quality=95)