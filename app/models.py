# app/models.py
from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base

class Dish(Base):
    __tablename__ = 'dishes'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    slug = Column(String, nullable=False, unique=True)
    image_url = Column(String)
    category = Column(String)
    in_stock = Column(Boolean, default=True)
