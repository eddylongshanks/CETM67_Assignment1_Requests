""" LTV Calculator Requests
"""

import json
from requests import post, get

# Calculator Endpoint
BASE_URL = "https://eposdjjkpd.execute-api.eu-west-2.amazonaws.com/dev"


acceptable_ltv_data = {
    "loan_amount": 40000, 
    "property_value": 100000
}

not_acceptable_ltv_data = {
    "loan_amount": 90000, 
    "property_value": 100000
}

response = post(BASE_URL + "/ltv-calculator-v1", json = acceptable_ltv_data)
print("POST Acceptable LTV Request...")
print("Response: " + response.text)

response = post(BASE_URL + "/ltv-calculator-v1", json = not_acceptable_ltv_data)
print("POST Not Acceptable LTV Request...")
print("Response: " + response.text)
