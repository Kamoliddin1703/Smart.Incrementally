from sqlalchemy.orm import Session # type: ignore
from . import models, schemas
from .utils import get_password_hash # type: ignore


# CRUD для Items (Товары)
def create_item(db: Session, item: schemas.ItemCreate):
    """Создание нового товара."""
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 10):
    """Получение списка товаров с пагинацией."""
    return db.query(models.Item).offset(skip).limit(limit).all()

# CRUD для Ads (Рекламы)
def create_ad(db: Session, ad: schemas.AdCreate):
    """Создание новой рекламы."""
    db_ad = models.Ad(**ad.dict())
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad

def get_ads(db: Session, skip: int = 0, limit: int = 10):
    """Получение списка реклам с пагинацией."""
    return db.query(models.Ad).offset(skip).limit(limit).all()

# CRUD для Blogs (Блоги)
def create_blog(db: Session, blog: schemas.BlogCreate):
    """Создание нового блога."""
    db_blog = models.Blog(**blog.dict())
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    """Получение списка блогов с пагинацией."""
    return db.query(models.Blog).offset(skip).limit(limit).all()

# CRUD для Videos (Видео)
def create_video(db: Session, video: schemas.VideoCreate):
    """Создание нового видео."""
    db_video = models.Video(**video.dict())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def get_videos(db: Session, skip: int = 0, limit: int = 10):
    """Получение списка видео с пагинацией."""
    return db.query(models.Video).offset(skip).limit(limit).all()

# CRUD для Users (Пользователи)
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password),
        birthdate=user.birthdate,
        gender=user.gender,
        phone_number=user.phone_number,
        secondary_email=user.secondary_email,
        region=user.region,
        birthplace=user.birthplace
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    """Получение пользователя по ID."""
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    """Получение пользователя по username."""
    return db.query(models.User).filter(models.User.username == username).first()

# Добавляем функцию для поиска пользователя по email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    """Получение списка пользователей с пагинацией."""
    return db.query(models.User).offset(skip).limit(limit).all()

