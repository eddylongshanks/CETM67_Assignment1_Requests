""" Script for LTV Calculator API
"""

import requests, json

BASE_URL = "https://mgyoz0j5fk.execute-api.us-east-1.amazonaws.com/default/ld-ltvcalculator"

# Send Request
data = json.dumps({"loan_amount": 20000, "property_value": 120000})
response = requests.post(BASE_URL, data)

# Parse response to JSON
response_data = json.loads(response.text)

# Access message body
response_body = response_data['body']

print(response_data)
print("\nLTV Percentage: " + str(response_body['ltv_percentage']))
