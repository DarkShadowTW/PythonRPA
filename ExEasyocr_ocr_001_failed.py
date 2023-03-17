#Failed
#ImportError: Something is wrong with the numpy installation. While importing we detected an older version of numpy in ['C:\\Users\\eric4\\.conda\\envs\\python_rpa_371\\lib\\site-packages\\numpy']. One method of fixing this is to repeatedly uninstall numpy until none is found, then reinstall this version.

import easyocr

reader = easyocr.Reader(['en'])  # 創建一個OCR讀取器，設置要識別的語言為英文
result = reader.readtext('images/ocr_numeric.png')  # 讀取圖片並識別文字
print(result)  # 輸出識別結果