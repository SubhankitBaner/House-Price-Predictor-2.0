# 🏡 House Price Predictor (v2)

This is an improved version of my earlier House Price Prediction app, now featuring a cleaner interface, more user-friendly controls, and a broader set of input features to generate better predictions.

---

## 🚀 Overview

This web app predicts house prices using a trained **Ridge Regression** model. It's built with **Streamlit** and allows users to input housing characteristics to estimate the property's market value instantly.

---

## ✅ Key Features

- 🧠 Ridge Regression model chosen after testing multiple regression algorithms.
- ✨ New features added: Basement, Guest Room, Preferred Area, Furnishing Level, etc.
- 🎯 Optimized and interactive UI using column-based layout.
- 🧪 Input validation to ensure values remain within valid ranges.
- 🌀 Spinner animation while model predicts.
- 📏 Currency output formatted in Indian Rupees (INR).

---

## 📊 Model Performance

After evaluating several machine learning models, **Ridge Regression** was selected due to its performance on both training and test data.

### 🔍 Ridge Regression Evaluation:

#### Train Performance
- **MAE**: 677,028.69  
- **R² Score**: 0.704  

#### Test Performance
- **MAE**: 987,143.74  
- **R² Score**: 0.650  

> ⚠️ **Note**: While results aren't perfect, the dataset may be a limiting factor. Nonetheless, the model performs reliably for general use cases.

---

## 🖼️ Screenshot

Here’s a preview of the app interface:

![App Screenshot](images/screenshot.png)

---

## 📁 Project Structure
├── app.py 
├── model/
│ └── model_pipeline.pkl 
├── dataset/
│ └── Housing.csv 
├── images/
│ ├── house.webp 
│ └── screenshot.png 
├── requirements.txt 
└── README.md
