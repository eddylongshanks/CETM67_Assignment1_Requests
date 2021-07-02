""" oDip API
"""

from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
from requests import post
import json

SNS_API = "https://fm6o6wnr3l.execute-api.eu-west-2.amazonaws.com/dev/send"
API_KEY = "G5MWtixDKN3xgHcJkWqfc6tTa1a3ZBIv5TE2dVKZ"
API_HEADERS = {"x-api-key":API_KEY}

app = Flask(__name__)
api = Api(app)

class SendEnquiry(Resource):
    def post(self):
        try:            
            data = request.json

            # dump the data to a json string and then reload it back into json
            # helps to identify invalid json data
            json_data = json.loads(json.dumps(data))

            response = post(SNS_API, headers=API_HEADERS, json=json_data)

            log(response.text)

            response_message = str(response.text)
            return response_object(response.status_code, response_message)

        except Exception as e:
            log(e)
            response_message = str(type(e).__name__) + ": " + str(e)
            return response_object(500, response_message)


class GetLog(Resource):
    def get(self):
        f = open('odip_log.txt', 'r')
        return f.read()


class HealthCheck(Resource):
    def get(self):
        response_message = 'oDip API Available'
        return response_object(200, response_message)

## Routing ##
api.add_resource(SendEnquiry, '/send-enquiry')
api.add_resource(GetLog, '/log')
api.add_resource(HealthCheck, '/')

# Methods

def log(data_to_save):
    # Logs data to a local file for debugging
    with open('odip_log.txt', 'w') as log_file:
        log_file.write(str(data_to_save))
   
def response_object(status_code, message):
    # encapsulates the return object
    return {
        'statusCode': status_code,
        'body': message
    }

if __name__ == "__main__":
    app.run(debug=True, port=5001)