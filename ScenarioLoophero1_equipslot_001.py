import LibRPA as rpa
from PIL import ImageGrab

def main():
    # Pycharm PROJECT PythonRPA 縮到最小
    rpa.minimize_window("PythonRPA")
    rpa.maximize_window("LOOP HERO")

    g_loophero_image = "images/loophero_blood_exp.jpg"
    g_confidence = 0.8

    while True:
        b_find, l_pos = rpa.pic_exist_pos(g_loophero_image, g_confidence)
        if b_find == True:
            l_x = l_pos[0] - 275
            l_y = l_pos[1] - 238
            l_right = l_x + 315
            l_bottom = l_y + 236
            im = ImageGrab.grab(bbox=(l_x, l_y, l_right, l_bottom))
            im.save('temp/screenshot.png', quality=95)

            break

    rpa.maximize_window("PythonRPA")

    print("END")

if __name__ == '__main__':
    main()