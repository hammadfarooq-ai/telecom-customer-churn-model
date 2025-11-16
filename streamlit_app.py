import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.title("📊 Telco Customer Churn Prediction App")

model = joblib.load("model/model.pkl")

st.write("Provide customer information:")

senior = st.selectbox("Senior Citizen", [0, 1])
tenure = st.number_input("Tenure (months)", 0, 72)
charges = st.number_input("Monthly Charges", 0.0, 200.0)
total = st.number_input("Total Charges", 0.0, 10000.0)
contracts = st.selectbox("Contract", [0,1,2])  
online = st.selectbox("Online Security", [0,1])
tech = st.selectbox("Tech Support", [0,1])
payment = st.selectbox("Payment Method", [0,1,2,3])

input_data = np.array([senior, tenure, charges, total, contracts, online, tech, payment]).reshape(1, -1)

if st.button("Predict"):
    pred = model.predict(input_data)[0]
    if pred == 1:
        st.error("❌ Customer is likely to churn.")
    else:
        st.success("✔ Customer will stay.")
