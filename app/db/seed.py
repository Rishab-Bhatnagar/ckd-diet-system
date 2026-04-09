from app.db.session import SessionLocal
from app.models.ckd_stage import CKDStage
from app.models.food_item import FoodItem


def seed_ckd_stages():
    db = SessionLocal()

    stages = [
        CKDStage(stage=1, protein_limit=0.8, sodium_limit=2300, potassium_limit=3500, fluid_limit=2000),
        CKDStage(stage=2, protein_limit=0.8, sodium_limit=2000, potassium_limit=3000, fluid_limit=1800),
        CKDStage(stage=3, protein_limit=0.7, sodium_limit=1800, potassium_limit=2500, fluid_limit=1500),
        CKDStage(stage=4, protein_limit=0.6, sodium_limit=1500, potassium_limit=2000, fluid_limit=1200),
        CKDStage(stage=5, protein_limit=0.6, sodium_limit=1200, potassium_limit=1500, fluid_limit=1000),
    ]

    for stage in stages:
        existing = db.query(CKDStage).filter(CKDStage.stage == stage.stage).first()
        if not existing:
            db.add(stage)

    db.commit()
    db.close()


def seed_food_items():
    db = SessionLocal()

    foods = [
    # Breakfast items
    FoodItem(name="Roti", calories=120, protein=3, sodium=5, potassium=80, sugar=0),
    FoodItem(name="Poha", calories=180, protein=4, sodium=200, potassium=150, sugar=2),
    FoodItem(name="Upma", calories=200, protein=5, sodium=250, potassium=120, sugar=1),
    FoodItem(name="Idli", calories=70, protein=2, sodium=100, potassium=50, sugar=0),
    FoodItem(name="Dosa", calories=150, protein=3, sodium=200, potassium=100, sugar=1),

    # Main meals
    FoodItem(name="Dal", calories=230, protein=9, sodium=300, potassium=350, sugar=2),
    FoodItem(name="Boiled Rice", calories=130, protein=2.5, sodium=1, potassium=35, sugar=0),
    FoodItem(name="Vegetable Sabzi", calories=150, protein=3, sodium=200, potassium=250, sugar=3),
    FoodItem(name="Paneer", calories=265, protein=18, sodium=20, potassium=100, sugar=2),
    FoodItem(name="Curd", calories=98, protein=3.5, sodium=40, potassium=150, sugar=4),

    # Light foods
    FoodItem(name="Apple", calories=52, protein=0.3, sodium=1, potassium=107, sugar=10),
    FoodItem(name="Papaya", calories=43, protein=0.5, sodium=2, potassium=182, sugar=8),
    FoodItem(name="Cucumber", calories=16, protein=0.7, sodium=2, potassium=150, sugar=2),

    # Avoid-heavy foods (for contrast)
    FoodItem(name="Pickle", calories=50, protein=1, sodium=1500, potassium=50, sugar=2),
    FoodItem(name="Fried Snacks", calories=300, protein=4, sodium=500, potassium=200, sugar=3),
]

    for food in foods:
        existing = db.query(FoodItem).filter(FoodItem.name == food.name).first()
        if not existing:
            db.add(food)

    db.commit()
    db.close()


def seed_all():
    seed_ckd_stages()
    seed_food_items()