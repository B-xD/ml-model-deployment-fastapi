from fastapi import FastAPI
import joblib
import numpy as np 
from pathlib import Path
import pandas as pd
from pydantic import BaseModel
from typing import List  # <-- add this

# Define the request schema
'''class ChurnRequest(BaseModel):
    features: List[float | str]'''

BASE_DIR = Path(__file__).resolve().parent

churn_model = joblib.load(BASE_DIR / "churn_model.joblib")

#class_names = np.array(['Current', 'defaulted'])

app = FastAPI()

@app.get('/')
def reed_root():
    return{'message': 'Mortgage payment model API'}

#send the data to the model 
@app.post('/predict')
def predict(data: dict):
    df = pd.DataFrame([data]) 

    churn_prob = churn_model.predict_proba(df)[0, 1]

    return round(float(churn_prob),4)

