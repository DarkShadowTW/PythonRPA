import LibRPA as rpa
from PIL import ImageGrab

#從血和經驗往下找裝備清單

# constant
g_equipment_width = 296
g_equipment_height = 218

g_loophero_image = "images/loophero_blood_exp.jpg"
g_confidence = 0.8

# Equipment Slot
g_weapon_pos = []  # [0, 0, 0, 0, 0, 0]  #x, y, right, bottom, center_x, center_y

def set_weapson_pos(p_num, p_x, p_y):
    l_equipment_slot_pos = [0, 0, 0, 0, 0, 0]  # x, y, right, bottom, center_x, center_y
    l_equipment_slot_pos[0] = p_x
    l_equipment_slot_pos[1] = p_y
    l_equipment_slot_pos[2] = p_x + (g_equipment_width // 4)  # 取整數
    l_equipment_slot_pos[3] = p_y + (g_equipment_height // 3)
    l_equipment_slot_pos[4] = p_x + (l_equipment_slot_pos[2] // 2)
    l_equipment_slot_pos[5] = p_y + (l_equipment_slot_pos[3] // 2)

    return l_equipment_slot_pos

def main():
    # Pycharm PROJECT PythonRPA 縮到最小
    rpa.minimize_window("PythonRPA")
    rpa.maximize_window("LOOP HERO")

    while True:
        b_find, l_pos = rpa.pic_exist_pos(g_loophero_image, g_confidence)
        if b_find == True:
            l_x = l_pos[0] - 260
            l_y = l_pos[1] + 71
            l_right = l_x + g_equipment_width
            l_bottom = l_y + g_equipment_height
            im = ImageGrab.grab(bbox=(l_x, l_y, l_right, l_bottom))
            im.save('temp/equipment.png', quality=95)

            for i in range(1, 13):
                if i == 1 or i == 2 or i == 3 or i == 4:
                    l_x_tmp, l_y_tmp = l_x + ( g_equipment_width // 4 * (i - 1) ), l_y
                elif i == 5 or i == 6 or i == 7 or i == 8:
                    l_x_tmp, l_y_tmp = l_x + ( g_equipment_width // 4 * (i - 5) ), l_y + ( g_equipment_width // 4 * 1 )
                elif i == 9 or i == 10 or i == 11 or i == 12:
                    l_x_tmp, l_y_tmp = l_x + ( g_equipment_width // 4 * (i - 9) ), l_y + ( g_equipment_width // 4 * 2 )

                l_equipment_slot_pos = set_weapson_pos(i, l_x_tmp, l_y_tmp)

                im = ImageGrab.grab(bbox=(l_equipment_slot_pos[0], l_equipment_slot_pos[1], l_equipment_slot_pos[2], l_equipment_slot_pos[3]))
                im.save('temp/equipment' + str(i) + '.png', quality=95)

                g_weapon_pos.append(l_equipment_slot_pos)

            print(g_weapon_pos)
            break

    rpa.maximize_window("PythonRPA")

    print("END")

if __name__ == '__main__':
    main()