import os

import cv2


def resize_for_format(input_path, fmt, filename, rembg=False):
    sizes = {
        "square": (1080, 1080),
        "post": (1080, 1440),     # 3:4
        "vk_post": (1920, 1080),  # 16:9
    }

    target_w, target_h = sizes[fmt]

    # если фон удалялся — корректный путь уже придёт в input_path
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)

    # ресайз под нужный формат
    resized = cv2.resize(img, (target_w, target_h), interpolation=cv2.INTER_AREA)

    # возвращаем массив, чтобы дальше можно было PAD / дорисовку
    return resized

