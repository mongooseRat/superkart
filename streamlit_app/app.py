import streamlit as st
import requests

API_URL = "http://localhost:7860/predict"  # update if deployed remotely

st.set_page_config(page_title="SuperKart Sales Predictor", layout="centered")
st.title("🛒 SuperKart — Product Store Sales Prediction (2026)")
st.write("Enter product and store details to predict 'Product_Store_Sales_Total'.")

# -----------------------------
# Input form
# -----------------------------
with st.form("prediction_form"):
    Product_Weight = st.number_input("Product Weight", min_value=0.0, step=0.1)
    Product_Sugar_Content = st.selectbox("Sugar Content", ["Low Sugar", "No Sugar", "Regular", "reg"])
    Product_Allocated_Area = st.number_input("Allocated Area", min_value=0.0, step=0.001)
    Product_MRP = st.number_input("MRP", min_value=0.0, step=0.1)
    Store_Size = st.selectbox("Store Size", ["High", "Medium", "Small"])
    Store_Location_City_Type = st.selectbox("City Type", ["Tier 1", "Tier 2", "Tier 3"])
    Store_Type = st.selectbox("Store Type", ["Departmental Store", "Food Mart", "Supermarket Type1", "Supermarket Type2"])
    Store_Age_Years = st.number_input("Store Age (Years)", min_value=0, step=1)
    Product_Type_Category = st.selectbox("Product Type Category", ["Non Perishables", "Perishables"])

    submitted = st.form_submit_button("Predict Sales")

# -----------------------------
# Call API and display result
# -----------------------------
if submitted:
    payload = {
        "Product_Weight": Product_Weight,
        "Product_Sugar_Content": Product_Sugar_Content,
        "Product_Allocated_Area": Product_Allocated_Area,
        "Product_MRP": Product_MRP,
        "Store_Size": Store_Size,
        "Store_Location_City_Type": Store_Location_City_Type,
        "Store_Type": Store_Type,
        "Store_Age_Years": Store_Age_Years,
        "Product_Type_Category": Product_Type_Category
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            pred = result.get("Predicted_Product_Store_Sales_Total", None)
            if pred is not None:
                st.success(f"📈 Predicted Product Store Sales Total: **{pred:,.2f}**")
            else:
                st.error("API returned no prediction.")
        else:
            st.error(f"API error: {response.status_code} — {response.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")