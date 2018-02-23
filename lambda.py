import boto3

arn='INSERT ARN HERE'
subject='Customer Monthly Patching'
message="""Monthly patching ticket for Customer

Set this email to contact CUSTOMER EMAIL and remove no-reply@sns.amazonaws.com

Please follow the patching procedures as documented in the customer runbook

This is an automated message.
"""

def lambda_handler(event, context):
    client = boto3.client('sns')

    response = client.publish(
        TopicArn=arn,
        Subject=subject,
        Message=message
    )