from .database import SessionLocal
from . import models

db = SessionLocal()
blogs = db.query(models.Blog).all()
for blog in blogs:
    print(blog.title, blog.content)