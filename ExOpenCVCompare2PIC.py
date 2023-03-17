import cv2
from PIL import Image, ImageOps

# 用Pillow讀取圖片
img2 = Image.open('equipment/armor_2.png')
# 取得圖片大小
width, height = img2.size

# 捕獲圖片左下方1/3部分
img2 = img2.crop((2, 2 * height // 3, width // 3 - 5, height - 4))
img2.show()
img2.save('temp/armor_2_tmp.png')

# 讀取兩張圖片
img1 = cv2.imread('equipment/armor_2.png')
img2 = cv2.imread('images/5.png')

# 將圖片轉換成灰度圖像
gray_img1 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 利用 matchTemplate 函数比較圖片相似度
res = cv2.matchTemplate(gray_img1, gray_img2, cv2.TM_CCOEFF_NORMED)

# 比較結果中的最大值即為兩張圖片的相似度
similarity = cv2.minMaxLoc(res)[1]

# 如果相似度超過某個閾值，則認為圖片存在於另一張圖片中
threshold = 0.9
if similarity > threshold:
    print("圖片存在於另一張圖片中")
else:
    print("圖片不存在於另一張圖片中")