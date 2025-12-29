# backend/app/schemas.py
from pydantic import BaseModel

class CarInput(BaseModel):
    brand: str
    year: int
    kilometers_driven: int

class PredictionResponse(BaseModel):
    predicted_price: float
