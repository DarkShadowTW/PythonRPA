from PIL import Image

# 用Pillow讀取圖片
img = Image.open('equipment/armor_1.png')
img.show()

# 取得圖片大小
width, height = img.size

# 捕獲圖片左下方1/3部分
crop = img.crop((2, 2 * height // 3, width // 3 - 5, height - 4))
crop.show()
crop.save('temp/5.png')