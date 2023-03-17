#Failed

import pytesseract
from PIL import Image, ImageOps

# 用Pillow讀取圖片
img = Image.open('equipment/armor_1.png')

# 取得圖片大小
width, height = img.size

# 捕獲圖片左下方1/3部分
crop = img.crop((2, 2 * height // 3, width // 3 - 5, height - 4))
crop.show()

scale = 1 # 放大倍數
new_width = width * scale
new_height = height * scale

# 執行圖像縮放
resized_img = crop.resize((new_width, new_height))
resized_img.show()

# 反轉圖片
inverted_img = ImageOps.invert(resized_img)
# 顯示反轉後的圖片
inverted_img.show()

# 使用Tesseract識別圖片中的文字
text = pytesseract.image_to_string(inverted_img)

# 輸出識別的文字
print(text)