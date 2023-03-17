import pytesseract
from PIL import Image

# 用Pillow讀取圖片
img = Image.open('images/ocr_numeric.png')
img.show()

# 使用Tesseract識別圖片中的文字
text = pytesseract.image_to_string(img)

# 輸出識別的文字
print(text)