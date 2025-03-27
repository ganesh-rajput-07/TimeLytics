import streamlit as st
import joblib
import numpy as np
import gdown

# Google Drive file ID
file_id = "10eVzX0vGlTGWPp63un0w9t8iJn5QK-Jz"

# Direct download link
url = f"https://drive.google.com/uc?id={file_id}"

# Download model
gdown.download(url, "random_forest_model.pkl", quiet=False)

# Load model
rf_model = joblib.load("random_forest_model.pkl")

st.write("✅ Model loaded successfully!")


# Define mappings for categorical features
category_mapping = {"electronics": 0, "fashion": 1, "home": 2, "toys": 3}
shipping_mapping = {"standard": 0, "express": 1}

# Streamlit UI
st.title("Timelytics - Delivery Time Prediction")

# User Inputs
product_category = st.selectbox("Select Product Category", list(category_mapping.keys()))
customer_zip = st.number_input("Enter Customer Zip Code", min_value=10000, max_value=99999, step=1)
shipping_method = st.selectbox("Select Shipping Method", list(shipping_mapping.keys()))

# Additional Features (Dummy Inputs for Now)
purchase_year = st.number_input("Enter Purchase Year", min_value=2016, max_value=2025, step=1)
purchase_month = st.number_input("Enter Purchase Month", min_value=1, max_value=12, step=1)
purchase_day = st.number_input("Enter Purchase Day", min_value=1, max_value=31, step=1)

# Convert Inputs to Model Format
input_data = np.array([[  
    category_mapping[product_category],  # Product Category
    customer_zip,                        # Customer Zip Code
    shipping_mapping[shipping_method],   # Shipping Method
    purchase_year,                        # Purchase Year
    purchase_month,                       # Purchase Month
    purchase_day                           # Purchase Day
]])

# Make Prediction
if st.button("Predict Delivery Time"):
    predicted_time = rf_model.predict(input_data)
    st.success(f"Estimated Delivery Time: {predicted_time[0]:.2f} days")
