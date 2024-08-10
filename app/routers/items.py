# app/routers/items.py
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter

from .. import crud, schemas, models
from ..database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@router.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

# app/routers/ads.py
# аналогично для рекламы

# app/routers/blogs.py
# аналогично для блогов

# app/routers/videos.py
# аналогично для видео
