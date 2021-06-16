""" SNS Requests
"""

import json
from requests import post, get

BASE_URL = "http://127.0.0.1:5000"
#BASE_URL = "http://ec2-54-175-80-131.compute-1.amazonaws.com"

data = '{"first_name":"sns_api6","last_name":"Stevenson","telephone_number":"07777456278"}'

response = get(BASE_URL + "/get-topics")
print(response.text)

response = post(BASE_URL + "/send", json = data)
print(response.text)
