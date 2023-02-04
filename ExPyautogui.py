import pyautogui

def pic_exist(p_img_path, p_confidence):
    l_position = pyautogui.locateOnScreen(p_img_path, confidence=p_confidence)
    if l_position is not None:
        return True
    else:
        return False

def pic_moveto(p_img_path, p_confidence):
    l_position = pyautogui.locateOnScreen(p_img_path, confidence=p_confidence)
    if l_position is not None:
        pyautogui.moveTo(l_position[0], l_position[1], duration=0.2)


def pic_click(p_img_path, p_confidence, p_click_time):
    l_position = pyautogui.locateOnScreen(p_img_path, confidence=p_confidence)
    if l_position is not None:
        try:
            if p_click_time == 1:
                pyautogui.Click(l_position)
            else:
                pyautogui.doubleClick(l_position)
        except:
            print("doubleClick Failed", p_img_path)


g_loophero_image = "images/loophero.jpg"
g_confidence = 0.8
if pic_exist(g_loophero_image, g_confidence):
    pic_moveto(g_loophero_image, g_confidence)
    #pic_click(g_loophero_image, g_confidence, 2)