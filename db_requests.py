""" DB Requests
"""

import json
from requests import post, get

BASE_URL = "http://127.0.0.1:5000"

# GET request
response = get(BASE_URL + "/get-all-enquiries")
response_data = json.dumps(response.text)
print(response.text)

# print("Name: " + response_data['person-name'] + ", Age: " + response_data['age'] + ", Favourite Food: " + response_data['fav_food'])

# Expected Response

# [
#    {
#        'fav_food': 'Toast',
#        'person-name': 'Bob',
#        'age': '44'
#    }
# ]


# GET a specific item/person
# response = requests.get(BASE_URL + "/name/Steve")
# print(response.text)


# CREATE a new item
data = {
    'first_name': 'Steve',
    'last_name': 'Smith',
    'building': '11',
    'street': 'Indigo Avenue',
    'town': 'Newcastle',
    'county': 'Tyne and Wear',
    'postcode': 'NE2 3JM',
    'telephone_number': '07777777777',
    'email': 'me@me.com',
    'preferred_time_to_contact': 'S',
    'annual_income': '30000',
    'loan_amount': '50000',
    'property_value': '1000000',
    'mortgage_type': 'RM',
    'ltv_value': '50'
}

response = post(BASE_URL + "/add-enquiry", json = data)
print(response.text)
