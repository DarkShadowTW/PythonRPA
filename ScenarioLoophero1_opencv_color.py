#用 OpenCV 讀取圖片並判斷圖片的色系
import cv2
import numpy as np

#讀取圖片
image = cv2.imread('images_loophero/equipment1.png')

#將圖片轉換為HSV色彩空間
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定義藍色範圍
blue_lower = np.array([100, 50, 50])
blue_upper = np.array([130, 255, 255])

# 定義棕色範圍
brown_lower = np.array([10, 50, 20])
brown_upper = np.array([20, 255, 200])

# 定義灰色範圍
gray_lower = np.array([0, 0, 50])
gray_upper = np.array([180, 30, 200])

# 定義黃色範圍
yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])

# 定義橘色範圍
orange_lower = np.array([10, 100, 20])
orange_upper = np.array([25, 255, 255])

#創建遮罩
blue_mask = cv2.inRange(hsv_image, blue_lower, blue_upper)
brown_mask = cv2.inRange(hsv_image, brown_lower, brown_upper)
gray_mask = cv2.inRange(hsv_image, gray_lower, gray_upper)
yellow_mask = cv2.inRange(hsv_image, yellow_lower, yellow_upper)
orange_mask = cv2.inRange(hsv_image, orange_lower, orange_upper)

#獲取符合顏色範圍的像素
blue_pixels = cv2.countNonZero(blue_mask)
brown_pixels = cv2.countNonZero(brown_mask)
gray_pixels = cv2.countNonZero(gray_mask)
yellow_pixels = cv2.countNonZero(yellow_mask)
orange_pixels = cv2.countNonZero(orange_mask)

#判斷圖片中的主要顏色
max_pixels = max(blue_pixels, brown_pixels, gray_pixels, yellow_pixels, orange_pixels)

if max_pixels == blue_pixels:
    print("圖片主要顏色為藍色")
elif max_pixels == brown_pixels:
    print("圖片主要顏色為棕色")
elif max_pixels == gray_pixels:
    print("圖片主要顏色為灰色")
elif max_pixels == yellow_pixels:
    print("圖片主要顏色為黃色")
else:
    print("圖片主要顏色為橘色")