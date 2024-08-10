from sqlalchemy.orm import Session # type: ignore
from . import models, schemas

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