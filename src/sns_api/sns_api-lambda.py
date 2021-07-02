''' SNS Packager
'''

import json
import boto3
import botocore.exceptions

sns = boto3.client('sns')
topic_arn = 'arn:aws:sns:eu-west-2:659206698074:cetm67-odip-sub-v1-dev'

def lambda_handler(event, context):
    try:
        data = get_data(event)
        send_to_sns(data)
        
        response_message = "Message Sent, by SNS API"
        return response_object(200, response_message)

    except Exception as e:
        response_message = 'Error: ' + str(e) + ' event: ' + str(event)
        return response_object(500, response_message)
    
def get_data(event):
    # extracts data from the event body and returns it
    try:
        body = json.loads(event['body'])
        
        return body
    except:
        raise

def send_to_sns(data):
    # packages data into SNS message and publishes to the queue
    sns.publish(
        TopicArn=topic_arn,
        Message=json.dumps(data)
        )
  
def response_object(status_code, message):
    # encapsulates the return object
    return {
        'statusCode': status_code,
        'body': message
    }