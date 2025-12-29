import streamlit as st
import requests
import os

# In K8s this will be a service name; locally we can override
BACKEND_URL = os.getenv("BACKEND_URL", "http://car-backend:8000")

st.set_page_config(page_title="Second-Hand Car Price", page_icon="🚗")
st.title("🚗 Second-Hand Car Price Predictor")

brand = st.selectbox("Brand", ["honda", "hyundai", "maruti", "toyota"])
year = st.slider("Year", 2005, 2024, 2018)
kms = st.number_input("Kilometers Driven", 0, 300000, 60000, step=1000)

if st.button("Predict Price"):
    payload = {
        "brand": brand,
        "year": year,
        "kilometers_driven": kms
    }
    try:
        r = requests.post(f"{BACKEND_URL}/predict", json=payload, timeout=5)
        r.raise_for_status()
        price = r.json()["predicted_price"]
        st.success(f"💰 Estimated Price: ₹ {price:,}")
    except Exception as e:
        st.error(f"Backend not reachable: {e}")
