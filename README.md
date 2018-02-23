# AWS Lambda Cron Emailer
## by Cory Burns

<br /><br />
This is a simple snippet for configuring Lambda functions to send an email out on a scheduled basis, using CloudWatch as a cron. 
This can be useful for creating automating patching tickets for customers with manual patching or other repeatable, not automatable tasks

<br /><br />
This contains two files:

### iam_policy.json
This is the JSON for allowing your Lambda function to access CloudWatch and publish to your SNS
<br />
Replace "YOUR ARN HERE" with your Topic's ARN, no other changes required
  
### lambda.py
This is the actual Python code used in the Lambda function.  It is Python 3.6
<br />
Replace arn, subject, and message with your own content.
<br />
The example I have included is a sample patching ticket.