import json
import boto3
import os

ses_client = boto3.client('ses')

SENDER = os.environ.get("SENDER_EMAIL")
RECIPIENT = os.environ.get("RECIPIENT_EMAIL")

def lambda_handler(event, context):
    subject = "Hello from SES + SAM!"
    body_text = "This is a test email sent using AWS SES through a Lambda function."
    
    try:
        response = ses_client.send_email(
            Source=SENDER,
            Destination={'ToAddresses': [RECIPIENT]},
            Message={
                'Subject': {'Data': subject},
                'Body': {
                    'Text': {'Data': body_text}
                }
            }
        )
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent!", "MessageId": response['MessageId']})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
