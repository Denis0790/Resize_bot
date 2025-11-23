import cv2
import numpy as np


def add_pad(img: np.ndarray, target_size: tuple, color=(0, 0, 0)) -> np.ndarray:
    h, w = img.shape[:2]
    target_w, target_h = target_size

    # вычисляем паддинг
    pad_w = max(target_w - w, 0)
    pad_h = max(target_h - h, 0)
    top = pad_h // 2
    bottom = pad_h - top
    left = pad_w // 2
    right = pad_w - left

    # создаём canvas с тем же числом каналов, что и img
    channels = img.shape[2] if len(img.shape) > 2 else 1
    if len(color) != channels:
        color = tuple(list(color) + [0] * (channels - len(color)))

    canvas = np.full((target_h, target_w, channels), color, dtype=img.dtype)

    # координаты для вставки изображения на canvas
    y_offset = top
    x_offset = left

    canvas[y_offset:y_offset + h, x_offset:x_offset + w] = img
    return canvas
