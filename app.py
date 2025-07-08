import streamlit as st
import pickle
import pandas as pd

# Load models once
with open('Model/petrol_model.pkl', 'rb') as f:
    petrol_model = pickle.load(f)

with open('Model/diesel_model.pkl', 'rb') as f:
    diesel_model = pickle.load(f)

st.set_page_config(page_title="Fuel Price Prediction", page_icon="⛽")
st.title("⛽ Fuel Price Prediction App")

# Select fuel type
fuel_type = st.selectbox("Select Fuel Type", ["Petrol", "Diesel"])

# Enter number of oil barrels
oil_barrel = st.number_input(f"Enter number of oil barrels for {fuel_type}:", min_value=0.0, format="%.2f")

# Predict when button clicked
if st.button(f"Predict {fuel_type} Price", type='primary'):
    if oil_barrel <= 0:
        st.warning("⚠️ Please enter a valid oil barrel value greater than 0.")
    else:
        input_df = pd.DataFrame({'oil_barrel': [oil_barrel]})

        # Choose the correct model based on selection
        if fuel_type == "Petrol":
            prediction = petrol_model.predict(input_df)[0]
        else:
            prediction = diesel_model.predict(input_df)[0]

        confidence_range = prediction * 0.1

        st.success("✅ Prediction Complete!")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("💰 Predicted Price", f"₹{prediction:.2f}")
        with col2:
            st.metric("📊 Confidence Range (±10%)", f"₹{confidence_range:.2f}")
