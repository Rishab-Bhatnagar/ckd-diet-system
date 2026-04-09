from fastapi import APIRouter
from app.db.session import SessionLocal
from app.models.food_item import FoodItem

router = APIRouter()

@router.get("/foods")
def get_foods():
    db = SessionLocal()
    foods = db.query(FoodItem).all()
    db.close()

    return foods