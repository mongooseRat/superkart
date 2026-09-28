from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI(
    title="SuperKart Sales Prediction API",
    description="Predict weekly product store sales using the trained ML model.",
    version="1.0"
)

# -----------------------------
# Load trained model
# -----------------------------
MODEL_PATH = "superkart_best_model.joblib"
model = joblib.load(MODEL_PATH)

# -----------------------------
# EXACT feature order required by the model
# -----------------------------
FEATURE_COLUMNS = [
    "Product_Weight",
    "Product_Sugar_Content",
    "Product_Allocated_Area",
    "Product_MRP",
    "Store_Size",
    "Store_Location_City_Type",
    "Store_Type",
    "Store_Age_Years",
    "Product_Type_Category"
]

# -----------------------------
# Input schema
# -----------------------------
class SalesInput(BaseModel):
    Product_Weight: float
    Product_Sugar_Content: str
    Product_Allocated_Area: float
    Product_MRP: float
    Store_Size: str
    Store_Location_City_Type: str
    Store_Type: str
    Store_Age_Years: float
    Product_Type_Category: str

# -----------------------------
# Health check
# -----------------------------
@app.get("/")
def health():
    return {"status": "ok", "message": "SuperKart API running"}

# -----------------------------
# Prediction endpoint
# -----------------------------
@app.post("/predict")
def predict_sales(input_data: SalesInput):

    # Convert input to DataFrame in exact order
    df = pd.DataFrame([[getattr(input_data, col) for col in FEATURE_COLUMNS]],
                      columns=FEATURE_COLUMNS)

    # Run prediction
    pred = model.predict(df)[0]

    return {"Predicted_Product_Store_Sales_Total": float(pred)}