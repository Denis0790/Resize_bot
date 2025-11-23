import cv2
import os
import numpy as np


UPLOAD_FOLDER = "backend/static/uploads"


def generate_images(filename: str):  # считать файл и превратить в матрицу пикселей
    input_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(input_path):  # Проверить есть ли фото в папке:
        raise FileNotFoundError("Файл не найден")

    image = cv2.imread(input_path)  # матрица картинки

    if image is None:
        raise ValueError("Файл не является изображением")

    return image


def preprocess_numpy(image: np.ndarray) -> np.ndarray:
    img = image.astype(np.float32)  # Преобразование в float32
    img /= 255.0  # нормализация
    img = np.clip(img * 1.05, 0, 1)  # базовое увеличение контраста

    return img
