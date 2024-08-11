from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from .routers import items, ads, blogs, videos, users  # Импортируем роутер для пользователей

app = FastAPI()


# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Адрес вашего React-приложения
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(items.router)
app.include_router(ads.router)
app.include_router(blogs.router)
app.include_router(videos.router)
app.include_router(users.router)  # Подключаем роутер для пользователей

# Подключение статических файлов
app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def read_root():
    return {"message": "Welcome to Smart.Incrementally API"}