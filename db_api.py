""" Script for db API
"""

from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json
import boto3
import botocore.exceptions

dynamodb = boto3.resource('dynamodb')

app = Flask(__name__)
api = Api(app)

## Resources ##
class GetAllEnquiries(Resource):
    def get(self):
        # Get table
        try:
            table = dynamodb.Table('Enquiry')
            enquiries = table.scan()
            return enquiries['Items']
        except:
            return 'No table found'


class AddEnquiry(Resource):
    def post(self):
        try:
            data = request.json

            table = dynamodb.Table('Enquiry')
            table.put_item(
                Item = data
            )
            return 'Enquiry added'
        except:
            return 'Enquiry not added'


## Routing ##
api.add_resource(GetAllEnquiries, '/get-all-enquiries')
api.add_resource(AddEnquiry, '/add-enquiry')

if __name__ == "__main__":
    app.run(debug=True)