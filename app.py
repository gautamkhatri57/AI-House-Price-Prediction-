import streamlit as st
import joblib

st.html("""
        <style>
            .stApp{
             background-color: SteelBlue;
        }
        </style>
""")
model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction")

area = st.number_input("Area (sq ft)", 100, 100000)
bedrooms = st.number_input("Bedrooms", 1, 17)
bathrooms = st.number_input("Bathrooms", 1, 10)
stories = st.number_input("Stories", 1, 7)
parking = st.number_input("Parking", 0, 9)
age = st.number_input("age", 0, 50)
if st.button("Predict Price"):
    prediction = model.predict([[area, bedrooms, bathrooms, stories, parking]])
    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")