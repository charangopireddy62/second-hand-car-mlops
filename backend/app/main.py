# backend/app/main.py
from fastapi import FastAPI
from app.schemas import CarInput, PredictionResponse
from app.model import predict_price
from app.mlflow_utils import log_prediction

app = FastAPI(title="Second Hand Car Price API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict(car: CarInput):
    price = predict_price(
        brand=car.brand,
        year=car.year,
        kilometers_driven=car.kilometers_driven
    )

    log_prediction(
        params={
            "brand": car.brand,
            "year": car.year,
            "kilometers_driven": car.kilometers_driven
        },
        prediction=price
    )

    return PredictionResponse(predicted_price=price)
