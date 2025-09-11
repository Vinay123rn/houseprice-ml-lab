import streamlit as st
import joblib
import pandas as pd

st.title("🏠 House Price Predictor")

model = joblib.load("../model.pkl")

with st.form("predict"):
    locality = st.text_input("locality",)
    rent = st.number_input("Monthly Rent", value=15000)
    area = st.number_input("Square Feet", value=1000)
    
    bathrooms = st.number_input("bathrooms", value=2, min_value=0, max_value=10, step=1)
    parking = st.text_input("Parking (Open/Covered/Missing)", "Open")
    price_per_sqft = st.text_input("price_per_sqft (e.g., Downtown)", "Downtown")
    facing = st.text_input("facing",)
    BHK =st.number_input("BHK") 
    submitted = st.form_submit_button("Predict")

if submitted:
    X = pd.DataFrame([{
        "locality":locality,
        "rent": rent,
        "area": area,
        "BHK": BHK,
        " price_per_sqft":  price_per_sqft if  price_per_sqft else "Missing",
        "bathrooms": bathrooms,
        "parking": parking if parking else "Missing",
        "facing": facing
    }])
    pred = model.predict(X)[0]
    st.success(f"Predicted Price: {pred:,.2f}")
