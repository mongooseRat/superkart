**# SuperKart Sales Forecasting**



**Predict product‑store sales using a tuned XGBoost model.**



**## Features**

**- Flask API for predictions**

**- Streamlit front‑end**

**- 2026‑aligned store‑age logic**

**- Clean engineered features**



**## Run locally**

**bash**

**pip install -r api/requirements.txt**

**python api/app.py**







**# \*\*SuperKart Sales Prediction System - End‑to‑End ML Deployment\*\***



**SuperKart is a full end‑to‑end machine learning system that predicts \*\*weekly product‑level store sales\*\* using historical retail data.**  

**The project includes:**



**- A trained ML model**  

**- A production‑ready \*\*FastAPI\*\* backend served via \*\*Docker\*\***  

**- A user‑friendly \*\*Streamlit\*\* frontend**  

**- A complete data pipeline and training notebook**  

**- A fully documented GitHub repository**  



**This README provides everything needed to understand, run, and evaluate the project.**



**---**



**## \*\*1. Project Overview\*\***



**SuperKart predicts weekly sales for retail products based on:**



**- Product attributes**  

**- Store characteristics**  

**- Pricing**  

**- Allocated shelf area**  

**- City tier**  

**- Store type**  

**- Product category**  



**The goal is to help retail managers forecast demand, optimize inventory, and improve store‑level decision‑making.**



**The system is designed for \*\*real‑world deployment\*\*, with:**



**- A Dockerized API**  

**- A FastAPI prediction endpoint**  

**- A Streamlit UI for interactive predictions**  

**- A trained model stored as a `.joblib` artifact**  



**---**



**## \*\*2. Model Summary\*\***



**The model was trained using:**



**- \*\*Random Forest / XGBoost\*\***

**- One‑Hot Encoding for categorical variables**

**- Standard numeric preprocessing**

**- Hyperparameter tuning**

**- Train/validation/test split**



**The final model is saved as:**



**'superkart\_best\_model.joblib'**



**### \*\*Model Inputs (Features)\*\***



**The model expects the following features in this exact order:**



**1. Product\_Weight**  

**2. Product\_Sugar\_Content**  

**3. Product\_Allocated\_Area**  

**4. Product\_MRP**  

**5. Store\_Size**  

**6. Store\_Location\_City\_Type**  

**7. Store\_Type**  

**8. Store\_Age\_Years**  

**9. Product\_Type\_Category**  



**### \*\*Model Output\*\***



**The API returns:**



**'Predicted\_Product\_Store\_Sales\_Total'**



**---**



**## \*\*3. Repository Structure\*\***



**'superkart/**

**│**

**├── api/**

**│   ├── app.py                     # FastAPI backend**

**│   ├── Dockerfile                 # Production-ready Dockerfile**

**│   ├── requirements.txt           # Includes fastapi, uvicorn, pydantic**

**│   └── superkart\_best\_model.joblib**

**│**

**├── streamlit/**

**│   └── app.py                     # Streamlit frontend**

**│**

**├── notebooks/**

**│   └── model\_training.ipynb       # Full training workflow**

**│**

**├── data/**

**│   ├── raw/                       # Raw CSVs**

**│   └── processed/                 # Cleaned data**

**│**

**├── README.md                      # Project documentation**

**└── .gitignore**

**'**



**---**



**## \*\*4. FastAPI Backend (Dockerized)\*\***



**The backend is a FastAPI application served using \*\*Uvicorn\*\* inside Docker.**



**### \*\*Run the API using Docker\*\***



**From the 'api/' directory:**



**'**

**docker build -t superkart-api .**

**docker run -p 7860:7860 superkart-api**

**'**



**### \*\*API Documentation\*\***



**Once running, open:**



**'**

**http://localhost:7860/docs**

**'**



**You will see:**



**- Swagger UI**  

**- '/predict' endpoint**  

**- JSON schema**  

**- Try‑it‑out interface**  



**---**



**## \*\*5. Prediction Endpoint\*\***



**### \*\*POST /predict\*\***



**Example request:**



**'json**

**{**

&#x20; **"Product\_Weight": 1.2,**

&#x20; **"Product\_Sugar\_Content": "Regular",**

&#x20; **"Product\_Allocated\_Area": 20.0,**

&#x20; **"Product\_MRP": 199.99,**

&#x20; **"Store\_Size": "Medium",**

&#x20; **"Store\_Location\_City\_Type": "Tier 1",**

&#x20; **"Store\_Type": "Supermarket Type1",**

&#x20; **"Store\_Age\_Years": 12,**

&#x20; **"Product\_Type\_Category": "Perishables"**

**}**

**'**



**Example response:**



**'json**

**{**

&#x20; **"Predicted\_Product\_Store\_Sales\_Total": 5231.806640625**

**}**

**'**



**---**



**## \*\*6. Streamlit Frontend\*\***



**The Streamlit app provides a clean UI for entering product/store details and receiving predictions.**



**### \*\*Run Streamlit\*\***



**From the `streamlit/` directory:**



**'**

**streamlit run app.py**

**'**



**The app will automatically send POST requests to:**



**'**

**http://localhost:7860/predict**

**'**



**---**



**## \*\*7. How Everything Works Together\*\***



**1. \*\*User enters product/store details in Streamlit\*\***  

**2. Streamlit sends a \*\*POST\*\* request to FastAPI**  

**3. FastAPI validates the input using Pydantic**  

**4. The model receives the features in the correct order**  

**5. The model predicts weekly sales**  

**6. FastAPI returns the prediction**  

**7. Streamlit displays the result**  



**This is a fully functional ML deployment pipeline.**



**---**



**## \*\*8. Technologies Used\*\***



**- Python**  

**- Pandas**  

**- Scikit‑Learn**  

**- FastAPI**  

**- Uvicorn**  

**- Streamlit**  

**- Docker**  

**- Joblib**  

**- Pydantic**  



**---**



**## \*\*9. How to Reproduce the Project\*\***



**1. Clone the repository**  

**2. Install dependencies or build Docker image**  

**3. Run the FastAPI backend**  

**4. Run the Streamlit frontend**  

**5. Test predictions using '/docs' or Streamlit**  



**---**



**## \*\*10. Author\*\***



**\*\*CEASAR\*\***  

**Machine Learning Engineer**  

**Virginia, USA**  



**---**



**## \*\*11. Notes\*\***



**- The API only accepts \*\*POST\*\* requests**  

**- '/predict' will return \*\*405 Method Not Allowed\*\* if accessed via browser**  

**- All categorical values must match the model’s encoder categories**  

**- The model requires features in a specific order**  



**---**



**## \*\*12. Submission Checklist\*\***



**- \[x] Model trained and saved**  

**- \[x] FastAPI backend working**  

**- \[x] Docker container running**  

**- \[x] '/docs' reachable**  

**- \[x] Streamlit connected**  

**- \[x] Predictions verified**  

**- \[x] README completed**  

**- \[x] Repo ready for submission**  



**---**

