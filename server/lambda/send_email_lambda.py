import json
import boto3
import botocore

def lambda_handler(event, context):
    sender = 'yunmegan44@gmail.com'
    to_email = 'yunmegan44@gmail.com'
    subject = "Olive Cinema 영화 예매 알림"
    content = event['Records'][0]['body']
    content_type = 'Text'  # Html / Text
    

    client = boto3.client("ses", region_name="ap-northeast-2")

    try:
        response = client.send_email(
            Destination={
                "ToAddresses": [
                    to_email,
                ],
            },
            Message={
                "Body": {
                    content_type: {
                        "Charset": "UTF-8",
                        "Data": content,
                    }
                },
                "Subject": {
                    "Charset": "UTF-8",
                    "Data": subject,
                },
            },
            Source=sender,
        )
    except botocore.exceptions.ClientError as e:
        err_message = e.response.get("Error", {}).get("Message")
        print(err_message)
        return {
            'statusCode': 500,
            'body': json.dumps(err_message)
        }

    return {
        'statusCode': 200,
        'body': json.dumps('Success Message ID : ' + response.get('MessageId', ''))
    }