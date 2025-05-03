# random_forest_classifier_car_price.pkl

import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('random_forest_classifier_car_price.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🚗 Car Price Prediction App")
st.write("Predict car prices based on brand, year, mileage, and other features.")

# Hardcoded options based on your dataset
brands = ["Toyota", "Ford", "Honda", "Chevrolet", "Mercedes", "Audi", "Hyundai", "Kia", "Volkswagen", "BMW"]
models = [
    "Camry", "Civic", "CR-V", "RAV4", "Accord", "Corolla", "F-150", "Malibu", 
    "GLA", "Q5", "A4", "3 Series", "Golf", "Passat", "Tucson", "Sonata", 
    "Elantra", "Optima", "Rio", "Sportage", "Tiguan"
]
fuel_types = ["Petrol", "Diesel", "Hybrid", "Electric"]
transmissions = ["Manual", "Automatic", "Semi-Automatic"]
doors = [2, 3, 4, 5]
owner_counts = [1, 2, 3, 4, 5]

# Input fields
brand = st.selectbox("Brand", options=brands)
model_name = st.selectbox("Model", options=models)
year = st.number_input("Year", min_value=1990, max_value=2025, value=2020)
engine_size = st.number_input("Engine Size (L)", min_value=1.0, max_value=5.0, value=2.0)
fuel_type = st.selectbox("Fuel Type", options=fuel_types)
transmission = st.selectbox("Transmission", options=transmissions)
mileage = st.number_input("Mileage (km)", min_value=0, max_value=300000, value=50000)
doors = st.selectbox("Number of Doors", options=doors)
owner_count = st.selectbox("Owner Count", options=owner_counts)

# Prepare input as DataFrame
input_data = pd.DataFrame({
    "Brand": [brand],
    "Model": [model_name],
    "Year": [year],
    "Engine_Size": [engine_size],
    "Fuel_Type": [fuel_type],
    "Transmission": [transmission],
    "Mileage": [mileage],
    "Doors": [doors],
    "Owner_Count": [owner_count]
})

# Predict
if st.button("Predict Price"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"💰 Predicted Price: ${prediction:,.2f}")
    except Exception as e:
        st.error(f"Error: {e}")