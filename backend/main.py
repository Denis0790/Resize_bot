import uvicorn
from fastapi import FastAPI
from backend.routers import get_image_router

app = FastAPI()

app.include_router(get_image_router.router)  #роутер на приёмку изображения

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
