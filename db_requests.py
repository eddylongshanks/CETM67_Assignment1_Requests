""" DB Requests
"""

import requests, json
# import simplejson as json

BASE_URL = "http://127.0.0.1:5000"

# GET request
response = requests.get(BASE_URL)
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
response = requests.post(BASE_URL + "/name/Steve", json = {"person-name": "Steve", "age": "45", "fav_food": "pizza"})
print(response.status_code)
print(response.text)

# Expected Response

# 200
# "Person added!"