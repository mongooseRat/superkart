<<<<<<< HEAD
# **SuperKart — Product Store Sales Prediction System**

## **Summary**
SuperKart is a fully deployed machine‑learning system designed to predict **weekly product‑level store sales** for a retail environment. The project integrates data science, model development, API engineering, containerization, and frontend design into a single, production‑ready solution.

The system uses structured retail data — including product attributes, store characteristics, pricing, and city demographics — to generate accurate sales forecasts. After comprehensive preprocessing, feature engineering, and model evaluation, the final model was saved as a deployable artifact and exposed through a **FastAPI** prediction endpoint. The backend is fully containerized using **Docker**, ensuring reproducibility and seamless execution across environments.

A **Streamlit** frontend provides an intuitive interface for entering product and store details, sending requests to the API, and displaying predictions. End‑to‑end testing confirms reliable communication between the frontend and backend, with multiple prediction scenarios demonstrating correct model behavior and generalization.

SuperKart meets the requirements for an end‑to‑end ML deployment project:

- Data preparation and feature engineering  
- Model training, evaluation, and artifact saving  
- FastAPI backend with validated input schema  
- Dockerized deployment for reproducibility  
- Streamlit frontend for user interaction  
- Verified predictions across multiple test cases  
- Organized GitHub repository with full documentation  

SuperKart delivers a complete, real‑world machine‑learning pipeline capable of supporting retail decision‑making and operational forecasting.

---

# **Project Write‑Up**

## **1. Problem Definition**
Retail stores need accurate product‑level sales forecasts to optimize inventory, reduce stockouts, and improve revenue planning. Traditional forecasting methods often fail to incorporate product attributes, store characteristics, pricing, and city demographics.  
**SuperKart** addresses this by building a machine‑learning model that predicts **weekly product store sales** using structured retail data.

The goal is to deliver a fully deployed, real‑world ML system with:

- A trained predictive model  
- A FastAPI backend  
- A Dockerized API  
- A Streamlit frontend  
- Clear documentation and reproducibility  

---

## **2. Data Understanding & Preparation**
The dataset includes product‑level and store‑level attributes:

- Product weight  
- Sugar content category  
- Allocated shelf area  
- Maximum retail price (MRP)  
- Store size  
- Store location city tier  
- Store type  
- Store age  
- Product category  

### **Data Preparation Steps**
- Missing values handled appropriately  
- Categorical variables encoded using OneHotEncoder  
- Numeric variables scaled or left raw depending on model needs  
- Train/validation/test split performed  
- Final feature order preserved for deployment  

---

## **3. Model Development**
Multiple models were evaluated (Random Forest, Gradient Boosting, XGBoost).  
The final model was selected based on:

- Predictive performance  
- Stability  
- Generalization  
- Deployment compatibility  

The trained model was saved as:

```
superkart_best_model.joblib
```

---

## **4. Model Evaluation**
The model was evaluated using:

- RMSE  
- MAE  
- R²  
- Validation and test set performance  
- Error analysis across store types and product categories  

The model demonstrated strong predictive capability and generalized well across different store/product profiles.

---

## **5. Deployment Architecture**

### **A. FastAPI Backend**
- Defines `/predict` endpoint  
- Validates input using Pydantic  
- Loads the trained model  
- Returns predictions as JSON  

### **B. Docker Container**
- Ensures reproducible environment  
- Runs Uvicorn server inside container  
- Exposes port `7860`  

### **C. Streamlit Frontend**
- User inputs product/store details  
- Sends POST request to FastAPI  
- Displays predicted sales  

---

## **6. API Verification (Test Cases)**

### **Test Case 1 — High‑MRP, Large Store**
```
{
  "Predicted_Product_Store_Sales_Total": 3454.966552734375
}
```

### **Test Case 2 — Low‑MRP, Small Store**
```
{
  "Predicted_Product_Store_Sales_Total": 789.416748046875
}
```

These demonstrate correct schema handling, categorical encoding, numeric processing, and end‑to‑end prediction functionality.

---

## **7. System Integration**
Streamlit successfully communicates with FastAPI:

- Streamlit sends POST requests  
- FastAPI validates and processes input  
- Model predicts  
- Streamlit displays results  

Docker logs confirm:

```
POST /predict HTTP/1.1" 200 OK
```

---

## **8. Repository Structure**
```
superkart/
│
├── api/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── superkart_best_model.joblib
│
├── streamlit/
│   └── app.py
│
├── notebooks/
│   └── model_training.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
│
├── README.md
└── .gitignore
```

---

## **9. How to Run the API (Docker)**

### **Build the API container**
```
docker build -t superkart-api .
```

### **Run the container**
```
docker run -p 7860:7860 superkart-api
```

API will be available at:

```
http://localhost:7860/predict
```

---

## **10. How to Run Streamlit**
From the `streamlit/` directory:

```
streamlit run app.py
```

The UI will open in your browser.

---

## **11. Technologies Used**
- Python  
- Pandas  
- Scikit‑Learn  
- FastAPI  
- Uvicorn  
- Streamlit  
- Docker  
- Joblib  
- JSON  

---

## **12. Submission Checklist**
- [x] Model trained and saved  
- [x] API implemented  
- [x] Dockerfile created  
- [x] Streamlit UI implemented  
- [x] End‑to‑end tests completed  
- [x] README documented  
- [x] Repo structured and clean  
- [x] Predictions verified  
- [x] Project submitted  

---
>>>>>>> 068ffb1b50e2e4ececd0f71bcbe33f6e42e22390
