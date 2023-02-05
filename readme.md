環境建置
===

一、安裝
---
1. ANACONDA：https://repo.anaconda.com/archive/Anaconda3-2022.10-Windows-x86_64.exe
2. PYCHARM：https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC

二、環境配置
---

1. ANACONDA : 

>選擇 Create
![img.png](/readme/img.png)

>安裝 Python Version 3.7.13
![img_1.png](/readme/img_1.png)

>選擇 Open Terminal
![img_2.png](/readme/img_2.png)

>在 Terminal 視窗內安裝 Python 套件:
安裝 opencv  
pip install numpy==1.15.3  
pip install matplotlib==3.0.1  
pip install opencv-python==3.4.2.16  
pip install opencv-contrib-python==3.4.2.16  

>安裝 PyWin32 用於視窗相關控制  
pip install --ignore-installed --upgrade PyWin32  

>安裝 pyautogui 用於 RPA 相關操作  
pip install --ignore-installed --upgrade pyautogui

2. PYCHARM 設置 ANACONDA 

>建立新專，選擇 Add interpreter
![img_3.png](/readme/img_3.png)

>再 Anaconda 找到剛建立的環境
![img_4.png](/readme/img_4.png)

三、Download Source Code
---

https://github.com/DarkShadowTW/PythonRPA

．Ex*.py：達到各種 RPA 的範列程式  
．LibRPA.py：Library 將 RPA 程式寫好類 exist, click 等語法，以及目前畫面放大縮小  
．Scenario1.py：DEMO PROGRAM  


