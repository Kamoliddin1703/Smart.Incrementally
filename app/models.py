from sqlalchemy import Column, Integer, String, Float, Text # type: ignore
from .database import Base


class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    category = Column(String, index=True)  # Добавил индекс для категории


class Ad(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    image_url = Column(String, nullable=True)
    video_url = Column(String, nullable=True)
    discount = Column(Float, nullable=True)

    # Убедитесь, что либо image_url, либо video_url имеют значение
    def __init__(self, title, image_url=None, video_url=None, discount=None):
        if not image_url and not video_url:
            raise ValueError("Either image_url or video_url must be provided")
        self.title = title
        self.image_url = image_url
        self.video_url = video_url
        self.discount = discount


class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    author = Column(String, index=True)  # Добавил индекс для автора


class Video(Base):
    __tablename__ = "videos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    url = Column(String)
    description = Column(Text)