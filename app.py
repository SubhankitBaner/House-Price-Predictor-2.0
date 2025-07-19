import streamlit as st
import joblib
import pickle
import numpy as np
import pandas as pd  
import time 
from babel.numbers import format_currency

pipeline=joblib.load('model/model_pipeline.pkl')

#st.title("🏠 House Price Prediction App")
col1, col2 = st.columns([4, 6])
with col1:
    st.image("images/house.jpg", width=400)
with col2:
    st.markdown("<h1 style='padding-top: 35px;'>House Price Prediction App</h1>", unsafe_allow_html=True)

st.set_page_config(page_title="House Price Predictor", page_icon="🏡", layout="centered")
st.divider()
st.write("Welcome to the House Price Prediction App! This tool uses machine learning to estimate the selling price of a house based on key features provided by the user. By analyzing parameters such as the square footage area, number of bathrooms and bedrooms, total number of stories, presence of air conditioning, and available parking space, the model predicts a fair market price for the property. The application is powered by a regression algorithm trained on real-world housing data, making it a valuable tool for home buyers, sellers, and real estate professionals alike")
st.sidebar.title("ℹ️ About This App")
st.sidebar.markdown("This application is designed to provide quick and intelligent estimates of house prices based on key property features. By analyzing factors like square footage, number of bedrooms and bathrooms, floors, air conditioning availability, and parking space, the model delivers a data-driven prediction to help users understand potential market value.\n\n"

"\n \n This House Price Predictor 2.0 represents a significant advancement over previous versions. We've enhanced the underlying predictive model through more sophisticated algorithms and a refined feature engineering process, leading to even greater accuracy and reliability in its price estimations.")
st.divider()
st.markdown("<h2 style='color:teal;'>Enter House Details Below</h2>", unsafe_allow_html=True)
st.divider()
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Total Area of the House (in square feet)", min_value=1200, max_value=17000,step=5)
    bedroom = st.number_input("Number of Bedrooms", min_value=1, max_value=6,step=1)
    bathroom = st.number_input("Number of Bathrooms", min_value=1, max_value=4,step=1)
    stories = st.number_input("Number of Storeys", min_value=1, max_value=4,step=1)
    parking = st.number_input("Number of Parking Spaces", min_value=0, max_value=3,step=1)


with col2:
    mainroad_input = st.selectbox("Is the House Located on the Main Road?", ["Yes", "No"])
    guestroom_input = st.selectbox("Does the House Have a Guest Room?", ["Yes", "No"])
    basement_input = st.selectbox("Does the House Include a Basement?", ["Yes", "No"])
    hotwaterheating_input = st.selectbox("Is Hot Water Heating Available?", ["Yes", "No"])
    airconditioning_input = st.selectbox("Is Air Conditioning Installed?", ["Yes", "No"])
st.markdown("---")
st.subheader("Additional Features")
prefarea_input = st.selectbox("Is the House in a Preferred Area?", ["Yes", "No"])
is_furnished_input = st.selectbox("Is the House Fully Furnished?", ["Unfurnished", "Semi-Furnished","Furnished"])

mainroad = 1 if mainroad_input == "Yes" else 0
guestroom = 1 if guestroom_input == "Yes" else 0
basement = 1 if basement_input == "Yes" else 0
hotwaterheating = 1 if hotwaterheating_input == "Yes" else 0
airconditioning = 1 if airconditioning_input == "Yes" else 0
prefarea = 1 if prefarea_input == "Yes" else 0
if is_furnished_input == "Unfurnished":
    is_furnished = 0
elif is_furnished_input == "Semi-Furnished":
    is_furnished = 1
else:  
    is_furnished = 2



if st.button("Predict House Price"):
    if(area < 1200 or area > 17000 or
        bedroom < 1 or bedroom > 6 or
        bathroom < 1 or bathroom > 4 or
        stories < 1 or stories > 4 or
        parking< 0 or parking > 3):
        st.error("❌ One or more input values are outside the allowed range. Please check and try again.")
    else:
        with st.spinner('Predicting the house price...'):
            time.sleep(2)
            area = np.log1p(area)
            input_df = pd.DataFrame([[area, bedroom,bathroom,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,is_furnished]],
                        columns=['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom',
                                'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea',
                                'furnishingstatus_encoded'])
            prediction = pipeline.predict(input_df)[0]
            prediction = np.expm1(prediction)
            formatted_price = format_currency(prediction, 'INR', locale='en_IN')
            st.markdown(
            f"<div style='background-color: #214321; padding: 12px; border-radius: 5px; text-align: center;'>"  # Dark green background similar to st.success
            f"<span style='font-size: 1.65em; font-weight: bold; color: white;'>🏡 Predicted Price: {formatted_price}</span>"
            f"</div>",
            unsafe_allow_html=True
        )

        # Your existing disclaimer
        st.markdown(
            "<p style='font-size: 1.00em; color: #999;'>Note: This is an estimated price based on our model and should be used for informational purposes only. Actual market values may vary due to dynamic nature of real estate.</p>",
            unsafe_allow_html=True
        )
        st.balloons()


st.markdown("---")
st.markdown("Created with ❤️ by Subhankit (https://github.com/SubhankitBaner)")



