# backend/app/model.py
from datetime import datetime

BASE_PRICE = 500000  # base price in INR

BRAND_MULTIPLIER = {
    "maruti": 1.0,
    "hyundai": 1.1,
    "honda": 1.15,
    "toyota": 1.2
}

def predict_price(brand: str, year: int, kilometers_driven: int) -> float:
    current_year = datetime.now().year
    age = current_year - year

    brand_factor = BRAND_MULTIPLIER.get(brand.lower(), 0.9)

    price = (
        BASE_PRICE * brand_factor
        - (age * 20000)
        - (kilometers_driven * 0.5)
    )

    return max(price, 50000)  # floor price
