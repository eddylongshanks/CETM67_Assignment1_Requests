import os
from LTVCalculator import LTVCalculator

MAX_LTV = os.environ.get('MAX_LTV')

def lambda_handler(event, context):
    loan_amount = event['loan_amount']
    property_value = event['property_value']
    max_ltv = MAX_LTV
    
    ltv_calculator = LTVCalculator(loan_amount, property_value, max_ltv)
    
    ltv_percentage = ltv_calculator.get_value()
    is_acceptable = ltv_calculator.is_acceptable()
    
    data = {
        "ltv_percentage": ltv_percentage,
        "is_acceptable": is_acceptable
    }

    return {
        "statusCode": 200,
        "body": data
    }
    