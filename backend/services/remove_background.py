from PIL.Image import Image
from numpy import ndarray
from rembg import remove
from PIL import Image
import numpy as np
import cv2

UPLOAD_FOLDER = "backend/static/uploads"
PROCESSED_FOLDER = "backend/static/processed"


def remove_background(image: np.ndarray) -> Image.Image:
    # Конвертируем OpenCV (BGR) в PIL (RGB)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image_rgb)

    # Удаляем фон
    return remove(pil_image)


