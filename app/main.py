from fastapi import FastAPI

from app.core.logger import setup_logger

setup_logger()
from app.db.session import engine
from app.db.base import Base

# Import models (VERY IMPORTANT for table creation)
from app.models import ckd_stage, food_item

# Import seeder
from app.db.seed import seed_all

# Import routers
from app.api.stage import router as stage_router
from app.api.food import router as food_router

from app.api.recommend import router as recommend_router



# Create FastAPI app
app = FastAPI(title="CKD Diet Recommendation API")


# Include routers
app.include_router(stage_router)
app.include_router(food_router)
app.include_router(recommend_router)


# Startup event
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    seed_all()


# Root endpoint
@app.get("/")
def root():
    return {"message": "CKD Diet API is running 🚀"}