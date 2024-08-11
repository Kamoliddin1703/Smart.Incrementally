from pydantic import BaseModel, EmailStr, Field # type: ignore
from typing import Optional
from datetime import datetime

# Схема для создания и отображения рекламы
class AdBase(BaseModel):
    title: str
    image_url: Optional[str] = None
    video_url: Optional[str] = None
    discount: Optional[float] = None

class AdCreate(AdBase):
    pass

class Ad(AdBase):
    id: int

    class Config:
        orm_mode = True

# Схема для товаров
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

# Схема для блогов
class BlogBase(BaseModel):
    title: str
    content: str

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int

    class Config:
        orm_mode = True

# Схема для видео
class VideoBase(BaseModel):
    title: str
    url: str

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True

# Схема для пользователей
class UserBase(BaseModel):
    username: str
    email: EmailStr
    # Новые поля
    birthdate: Optional[datetime] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    secondary_email: Optional[EmailStr] = None
    region: Optional[str] = None
    birthplace: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True