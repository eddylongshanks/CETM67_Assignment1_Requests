""" Script for SNS API
"""

from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json
import boto3
import botocore.exceptions

sns = boto3.client('sns')
topic_arn = 'arn:aws:sns:us-east-1:118394980800:cetm67-odip-sub-v1-dev'

app = Flask(__name__)
api = Api(app)

## Resources ##
class GetTopics(Resource):
    def get(self):
        try:
            topics = sns.list_topics()
            print(topics["Topics"])
            return topics
        except:
            return 'No topics found'

class PublishMessage(Resource):
    def post(self):
        try:
            data = request.json
            print(data)

            sns.publish(
                TopicArn=topic_arn,
                Message=data
                )

            return "Success"
        except:
            raise


## Routing ##
api.add_resource(GetTopics, '/get-topics')
api.add_resource(PublishMessage, '/send')

if __name__ == "__main__":
    app.run(debug=True)