""" Script for db API
"""

from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json
import boto3
import botocore.exceptions

# BASE_URL = "https://mgyoz0j5fk.execute-api.us-east-1.amazonaws.com/default/ld-ltvcalculator"

dynamodb = boto3.resource('dynamodb')

app = Flask(__name__)
api = Api(app)

## Resources ##
class GetAllPeople(Resource):
    def get(self):
        # Get table
        try:
            TABLE = dynamodb.Table('people')
            ALL_PEOPLE = TABLE.scan()
            return ALL_PEOPLE['Items']
        except:
            return 'No table found!'


class GetAPerson(Resource):
    def get(self, name_of_person):
        # Get specific item from a table
        try:
            TABLE = dynamodb.Table('people')
            PERSON = TABLE.get_item(
                Key={
                    'person-name': 'Bob'
                }
            )
            return PERSON['Item']
        except:
            return 'No person with that name found!'


class AddPerson(Resource):
    def post(self, name_of_person):        
        # Get specific item from a table
        try:
            data = request.json
            print(data)

            TABLE = dynamodb.Table('people')
            TABLE.put_item(
                Item = data
            )
            return 'Person added!'
        except:
            return 'Person not added!'


## API Routing ##
api.add_resource(GetAllPeople, '/')
api.add_resource(GetAPerson, '/name/<string:name_of_person>')
api.add_resource(AddPerson, '/name/<string:name_of_person>')

if __name__ == "__main__":
    app.run(debug=True)