import json 
import requests


data = {
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

url = 'http://0.0.0.0:8000/predict'

data = json.dumps(data)
response = requests.post(url, data)
print(response.json())