from fastapi import APIRouter, HTTPException
from app.engine.ckd_engine import get_diet_recommendation

router = APIRouter()

@router.get("/recommend")
def recommend(stage: int, diabetes: bool = False, hypertension: bool = False):
    try:
        result = get_diet_recommendation(stage, diabetes, hypertension)

        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))