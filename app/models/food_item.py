from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class FoodItem(Base):
    __tablename__ = "food_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    calories = Column(Float)
    protein = Column(Float)
    sodium = Column(Float)
    potassium = Column(Float)
    sugar = Column(Float)