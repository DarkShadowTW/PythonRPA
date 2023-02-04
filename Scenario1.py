import LibRPA as rpa

#Pycharm PROJECT PythonRPA 縮到最小
rpa.minimize_window("PythonRPA")
rpa.maximize_window("LOOP HERO")

#判斷圖片是否存在，如果存在就移到該圖片的位置
g_loophero_image = "images/loophero.jpg"
g_pycharm_image = "images/pycharm.jpg"
g_unity_hub_image = "images/unity_hub.jpg"
g_confidence = 0.8
g_duration = 0.4

if rpa.pic_exist(g_pycharm_image, g_confidence):
    rpa.pic_moveto(g_pycharm_image, g_confidence, g_duration)
if rpa.pic_exist(g_unity_hub_image, g_confidence):
    rpa.pic_moveto(g_unity_hub_image, g_confidence, g_duration)
if rpa.pic_exist(g_loophero_image, g_confidence):
    rpa.pic_moveto(g_loophero_image, g_confidence, g_duration)
    #pic_click(g_loophero_image, g_confidence, 2)

rpa.maximize_window("PythonRPA")

print("finished")