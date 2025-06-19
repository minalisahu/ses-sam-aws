# Import required libraries
import json                  # For formatting the response as JSON
import boto3                 # AWS SDK for Python to interact with AWS services
import os                    # For accessing environment variables

# Create a client for Amazon SES (Simple Email Service)
ses_client = boto3.client('ses')

# Get sender and recipient email addresses from environment variables
SENDER = os.environ.get("SENDER_EMAIL")
RECIPIENT = os.environ.get("RECIPIENT_EMAIL")

# Main Lambda function handler
def lambda_handler(event, context):
    # Define the subject and body of the email
    subject = "Hello from SES + SAM!"
    body_text = "This is a test email sent using AWS SES through a Lambda function."
    
    try:
        # Try to send the email using SES
        response = ses_client.send_email(
            Source=SENDER,  # The verified email address you're sending from
            Destination={
                'ToAddresses': [RECIPIENT]  # The verified email address you're sending to
            },
            Message={
                'Subject': {
                    'Data': subject  # Subject of the email
                },
                'Body': {
                    'Text': {
                        'Data': body_text  # Body of the email (plain text)
                    }
                }
            }
        )

        # If successful, return status 200 with the SES message ID
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Email sent!",
                "MessageId": response['MessageId']
            })
        }

    except Exception as e:
        # If any error occurs (e.g., email not verified), return error message with status 500
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)  # Convert exception to string for JSON response
            })
        }
