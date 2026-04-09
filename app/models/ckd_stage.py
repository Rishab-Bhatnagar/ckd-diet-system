from sqlalchemy import Column, Integer, Float
from app.db.base import Base

class CKDStage(Base):
    __tablename__ = "ckd_stages"

    id = Column(Integer, primary_key=True, index=True)
    stage = Column(Integer, unique=True, nullable=False)

    protein_limit = Column(Float)     # grams/day
    sodium_limit = Column(Float)      # mg/day
    potassium_limit = Column(Float)   # mg/day
    fluid_limit = Column(Float)       # ml/day