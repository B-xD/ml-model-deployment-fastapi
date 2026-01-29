Production ML Churn Prediction API

This is a production-ready machine learning system for predicting customer mortgage payment default probability, built with:
XGBoost
Scikit-learn pipelines
FastAPI
Docker

This is a continuation of the following repository: https://github.com/B-xD/mortgage-loan-approval-risk-assessment-system
This completes an End-to-end ML pipeline (data loading → preprocessing → training → evaluation)
- Feature engineering with ColumnTransformer
- XGBoost churn classifier
- Probability-based predictions (predict_proba)
- REST API using FastAPI
- Dockerized inference service
- Client script for testing predictions

Instructions 
1. Build a Docker image 
$ docker build -t image_name 

2. Create and run and a container:
$ docker run --name container_name -p 8000:8000 image_name

3. The output will contain the following: 
INFO:     Uvicorn running on http://0.0.0.0:8000
- Run the url in your browser. If you see this message: “Mortgage payment model API,” then the model is successfully running in your Docker container 

4. Make predictions:
   
4.1 Via web interface (Chrome, etc):
- Run url http://0.0.0.0:8000/docs 
- Click predict, then try it out
- Input the data under Request body (Example value). 
- Click execute (the predictions will show under Response body
- Note: the data format has to be  in the format below: 

{
  "contacts_count_12_mon": 5,
  "months_inactive_12_mon": 6,
  "total_ct_chng_q4_q1": 0.60,
  "total_relationship_count": 4,
  "total_trans_ct": 35,
  "total_trans_amt": 4200,
  "total_revolving_bal": 1200,
  "avg_open_to_buy": 48800,
  "avg_utilization_ratio": 0.02,
  "marital_status": "Single",
  "gender": "F",
  "credit_limit": 50000,
  "income_category": "$120K+",
  "dependent_count": 0,
  "total_amt_chng_q4_q1": 0.55,
  "customer_age": 45
}

4.2. Via Python client: Run client.py 




