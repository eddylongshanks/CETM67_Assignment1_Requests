# CETM67 Assignment 1 - API Requests v1.0

## LTV Calculator

Accepts the following two values as JSON:

```python
{
    "loan_amount": 20000,
    "property_value": 100000
}
```

Returns the following data:

- LTV Percentage
- A Boolean value determining acceptance, based on minimum LTV value provided within an Environment Variable set on the Lambda function
