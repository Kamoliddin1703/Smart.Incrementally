from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from typing import List
from .. import crud, models, schemas  # Исправленный путь импорта
from ..database import SessionLocal, engine

# Создаем все таблицы в базе данных, если они еще не созданы
models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Получение сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Создание рекламы
@router.post("/ads/", response_model=schemas.Ad)
def create_ad(ad: schemas.AdCreate, db: Session = Depends(get_db)):
    if not ad.image_url and not ad.video_url:
        raise HTTPException(status_code=400, detail="Either image_url or video_url must be provided.")
    return crud.create_ad(db=db, ad=ad)

# Получение списка реклам
@router.get("/ads/", response_model=List[schemas.Ad])
def read_ads(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    ads = crud.get_ads(db, skip=skip, limit=limit)
    return ads