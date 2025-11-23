import aiofiles
import os
import uuid

import cv2
from fastapi import APIRouter, UploadFile, File

from backend.services.add_pad import add_pad
from backend.services.image_generate_services import generate_images, preprocess_numpy
from backend.services.resize_img import resize_for_format
from backend.utils.helper import process_for_format

router = APIRouter(
    prefix='/image',
    tags=['Image Upload'],
)

UPLOAD_FOLDER = "backend/static/uploads"  # путь куда сохранить полученную картинку
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # создаст путь до картинки если не создана


@router.post("/upload")  # роутер на получение изображения
async def upload_image(image: UploadFile = File(...)):
    filename = f"{uuid.uuid4()}.jpg"  # создаем уникальное название картинки
    path = os.path.join(UPLOAD_FOLDER, filename)  # универсальный путь до места сохранения

    async with aiofiles.open(path, "wb") as f:  # запись картинки в размере 1мб
        while chunk := await image.read(1024 * 1024):
            await f.write(chunk)

    img = generate_images(filename)  # читаем картинку в cv2
    img = preprocess_numpy(img)  # нормализация (если нужна)

    results = []

    target_sizes = {
        "square": (1080, 1080),
        "post": (1080, 1440),
        "vk_post": (1920, 1080),
    }

    for fmt in ["square", "post", "vk_post"]:
        result = process_for_format(img, filename, fmt)  # удаление фона, промежуточное сохранение
        resized_img = resize_for_format(result["processed"], fmt, filename)  # массив NumPy
        padded_img = add_pad(resized_img, target_sizes[fmt])  # паддинг

        # финальное сохранение
        out_dir = f"backend/static/final/{fmt}"
        os.makedirs(out_dir, exist_ok=True)
        final_path = os.path.join(out_dir, filename)
        cv2.imwrite(final_path, padded_img, [cv2.IMWRITE_JPEG_QUALITY, 95])

        result["final"] = final_path
        results.append(result)

    return {"original": path, "results": results}





