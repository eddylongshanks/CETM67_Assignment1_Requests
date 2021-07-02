""" SNS Requests
"""

import json
from requests import post, get

BASE_URL = "https://fm6o6wnr3l.execute-api.eu-west-2.amazonaws.com/dev"
API_KEY = "G5MWtixDKN3xgHcJkWqfc6tTa1a3ZBIv5TE2dVKZ"
API_HEADERS = {"x-api-key":API_KEY}

data = {
	"first_name": "vs_SNS_API1",
	"email_address": "test@holmescentral.co.uk"
}

response = post(BASE_URL + "/send", headers=API_HEADERS, json = data)
print("POST New Enquiry... (/send)")
print("Response: " + response.text)