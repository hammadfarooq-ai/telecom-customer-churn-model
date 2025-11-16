# Telco Customer Churn Prediction Model

This model predicts whether a customer will churn based on telecom usage, contracts, payment methods, and service features.

## 📌 How Was the Model Trained?
- Dataset: Telco Customer Churn (Kaggle)
- Algorithm: RandomForestClassifier
- Data Preprocessing:
  - Categorical encoding (LabelEncoder)
  - Scaling numerical features
  - Handling missing values
  - Train-test split (80/20)

## 📦 Input Format
Provide an array of features matching the training order:
[SeniorCitizen, Tenure, MonthlyCharges, TotalCharges, Contract, OnlineSecurity, TechSupport, PaymentMethod]

## 🎯 Output
- **1 → Customer will churn**
- **0 → Customer will not churn**

## 👤 Author
Hammad Farooq

# 📘 Model Card: Telco Customer Churn Prediction

## 🧠 Model Summary
A machine learning classification model that predicts customer churn for telecom companies. Built using the Telco Customer Churn dataset on Kaggle.

## 🧪 Evaluation Metrics
- Accuracy: ~82%
- F1 Score: ~0.81
- Algorithm: RandomForestClassifier (300 trees)

## 📊 Intended Use
- Customer retention
- Fraud/behavior analysis
- Subscription churn tracking
- Telecom business insights

## ⚠ Limitations
- Limited to dataset quality
- Cannot guarantee future churn behavior
- Not suitable for high-risk decisions

## 👨‍💻 Developed By
**Hammad Farooq**  
Python Developer • Data Scientist

