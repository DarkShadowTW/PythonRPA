import LibRPA as rpa

######################################################
# 1. 縮小目前 Pychram by Python Project Name - PythonRPA
# 2. 指定要找的桌面 ICON (要改成你自己的 ICON)
# 3. 移動 Pycharm ICON, 移動到 Unity Hub ICON, 最後移動到 LOOP HERO ICON
# 4. 點擊 LOOP HERO ICON
#
# 相關程式來自 LibRPA Program
######################################################

#Pycharm PROJECT PythonRPA 縮到最小
def main():
    rpa.minimize_window("PythonRPA")

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
        rpa.pic_click(g_loophero_image, g_confidence, 2)

    print("finished")

if __name__ == '__main__':
    main()