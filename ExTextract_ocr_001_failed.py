import textract

print("OCR for ocr_numeric.png")

# 讀取文檔
text = textract.process('images/ocr_numeric.png')

# 輸出文本
print("RESULT:", text.decode('utf-8'))

print("OCR for 5.png")

text = textract.process('temp/5.png')

# 輸出文本
print("RESULT:", text.decode('utf-8'))

print("OCR for 5_2.png")

text = textract.process('temp/5_2.png')

# 輸出文本
print("RESULT:", text.decode('utf-8'))
