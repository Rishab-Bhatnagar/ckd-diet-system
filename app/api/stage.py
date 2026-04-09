from fastapi import APIRouter
from app.db.session import SessionLocal
from app.models.ckd_stage import CKDStage

router = APIRouter()

@router.get("/stages")
def get_stages():
    db = SessionLocal()
    stages = db.query(CKDStage).all()
    db.close()

    return stages