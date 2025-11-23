import os

import cv2

from backend.services.check_crop import AspectChecker
from backend.services.remove_background import remove_background
import numpy as np

PROCESSED_SQUARE = "backend/static/processed/square"
PROCESSED_POST = "backend/static/processed/post"
PROCESSED_VK = "backend/static/processed/vk_post"


def process_for_format(img, filename, fmt, tolerance=0.2):
    checker = AspectChecker(fmt, tolerance)
    h, w = img.shape[:2]

    need_remove = checker.need_remove_background(w, h)

    # Папка по формату
    if fmt == "square":
        save_dir = PROCESSED_SQUARE
    elif fmt == "post":
        save_dir = PROCESSED_POST
    else:
        save_dir = PROCESSED_VK

    os.makedirs(save_dir, exist_ok=True)

    name, _ = os.path.splitext(filename)

    if need_remove:
        save_path = os.path.join(save_dir, f"{name}_rembg.png")
        result_img = remove_background((img * 255).astype(np.uint8))
        result_img.save(save_path)
        status = "rembg"

    else:
        save_path = os.path.join(save_dir, f"{name}.jpg")
        cv2.imwrite(save_path, img)
        status = "norembg"

    return {
        "format": fmt,
        "status": status,
        "processed": save_path,
    }
