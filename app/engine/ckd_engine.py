from app.db.session import SessionLocal
from app.models.ckd_stage import CKDStage
from app.models.food_item import FoodItem
from app.core.logger import logger

def generate_reason_text(reasons):
    explanation_map = {
        "High protein exceeds CKD limit": "High protein can put extra load on kidneys.",
        "Moderate protein level": "Protein intake should be controlled in CKD.",
        "High sodium (BP risk)": "High sodium can increase blood pressure and harm kidney function.",
        "Moderate sodium level": "Sodium should be limited to avoid fluid retention.",
        "High potassium exceeds CKD limit": "High potassium can affect heart rhythm in kidney patients.",
        "Moderate potassium level": "Potassium should be monitored in CKD.",
        "High sugar (diabetes risk)": "High sugar can worsen diabetes and damage kidneys further.",
        "Moderate sugar level": "Sugar intake should be controlled."
    }

    return [explanation_map.get(r, r) for r in reasons]


def analyze_food(food, stage, diabetes=False, hypertension=False):
    reasons = []
    score = 0

    # Protein
    if food.protein > stage.protein_limit:
        reasons.append("High protein exceeds CKD limit")
        score += 2
    elif food.protein > 0.5 * stage.protein_limit:
        reasons.append("Moderate protein level")
        score += 1

    # Sodium
    sodium_limit = stage.sodium_limit
    if hypertension:
        sodium_limit *= 0.8

    if food.sodium > sodium_limit:
        reasons.append("High sodium (BP risk)")
        score += 2
    elif food.sodium > 0.5 * sodium_limit:
        reasons.append("Moderate sodium level")
        score += 1

    # Potassium
    if food.potassium > stage.potassium_limit:
        reasons.append("High potassium exceeds CKD limit")
        score += 2
    elif food.potassium > 0.5 * stage.potassium_limit:
        reasons.append("Moderate potassium level")
        score += 1

    # Diabetes
    if diabetes:
        if food.sugar > 10:
            reasons.append("High sugar (diabetes risk)")
            score += 2
        elif food.sugar > 5:
            reasons.append("Moderate sugar level")
            score += 1

    return score, reasons


def calculate_nutrition(foods):
    total = {"calories": 0, "protein": 0, "sodium": 0, "potassium": 0}

    for food in foods:
        total["calories"] += food.calories
        total["protein"] += food.protein
        total["sodium"] += food.sodium
        total["potassium"] += food.potassium

    return total


def build_meal(target_calories, primary_foods, fallback_foods, used_foods):
    selected = []
    current_calories = 0

    all_foods = primary_foods + fallback_foods

    for food in all_foods:
        if food.name in used_foods:
            continue

        selected.append({
            "name": food.name,
            "calories": food.calories
        })

        used_foods.add(food.name)
        current_calories += food.calories

        # stop if reached target OR at least 2 items
        if current_calories >= target_calories or len(selected) >= 2:
            break

    return selected


def generate_restrictions(stage, diabetes, hypertension):
    restrictions = [
        "Limit protein intake",
        "Control sodium consumption",
        "Monitor potassium levels"
    ]

    if diabetes:
        restrictions.append("Avoid high sugar foods")

    if hypertension:
        restrictions.append("Strictly reduce salt intake")

    return restrictions


def get_diet_recommendation(stage_number: int, diabetes=False, hypertension=False):
    logger.info(f"Generating diet for stage {stage_number}, diabetes={diabetes}, hypertension={hypertension}")
    db = SessionLocal()

    stage = db.query(CKDStage).filter(CKDStage.stage == stage_number).first()
    if stage:
        logger.info(f"Fetched CKD stage data: Stage {stage.stage}")
    else:
        logger.error("Invalid CKD stage provided")

    if not stage:
        db.close()
        return {"error": "Invalid stage"}

    foods = db.query(FoodItem).all()

    safe, moderate, avoid = [], [], []
    safe_food_objects = []
    moderate_food_objects = []
    for food in foods:
        score, reasons = analyze_food(food, stage, diabetes, hypertension)

        explanation = generate_reason_text(reasons if reasons else ["Safe within limits"])

        food_info = {
            "name": food.name,
            "explanation": explanation
        }

        if score <= 1:
            safe.append(food_info)
            safe_food_objects.append(food)
        elif score <= 3:
            moderate.append(food_info)
            moderate_food_objects.append(food)
        else:
            avoid.append(food_info)

    
   
    # 🎯 Calorie Target
    total_calories_target = 1500

    breakfast_target = total_calories_target * 0.3
    lunch_target = total_calories_target * 0.4
    dinner_target = total_calories_target * 0.3

# Meal planning
    used_foods = set()

    breakfast = build_meal(breakfast_target, safe_food_objects, moderate_food_objects, used_foods)
    lunch = build_meal(lunch_target, safe_food_objects, moderate_food_objects, used_foods)
    dinner = build_meal(dinner_target, safe_food_objects, moderate_food_objects, used_foods)

    # Nutrition
    nutrition_summary = calculate_nutrition(safe_food_objects)

    logger.info("Diet plan generated successfully")
    db.close()

    return {
        "stage": stage_number,
        "conditions": {
            "diabetes": diabetes,
            "hypertension": hypertension
        },
        "diet_plan": {
            "breakfast": breakfast,
            "lunch": lunch,
            "dinner": dinner
        },
        "nutrition_summary": nutrition_summary,
        "restrictions": generate_restrictions(stage, diabetes, hypertension),
        "recommendations": {
            "safe_foods": safe,
            "moderate_foods": moderate,
            "avoid_foods": avoid
        }
    }