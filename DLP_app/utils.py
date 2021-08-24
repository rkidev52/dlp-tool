import re
from .models import Message, Pattern
from django.conf import settings
import boto3
from asgiref.sync import sync_to_async
import asyncio
import slack
   
@sync_to_async
def get_patterns():
    patterns = list(Pattern.objects.all().values_list("pattern", flat=True).distinct())
    return patterns

@sync_to_async
def create_message(text, pattern):
    message = Message.objects.create(content=text, pattern=pattern)
    return message
   
def build_client_SQS():
    client_sqs = boto3.resource("sqs", region_name=settings.REGION_NAME, aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_KEY_ID)
    return client_sqs

def build_client_Slack():
    client_slack = slack.WebClient(token=settings.OAUTH_ACCESS_TOKEN)
    return client_slack

async def search_for_leaks(text, channel, ts):
    client_sqs = build_client_SQS()
    queue = client_sqs.get_queue_by_name(QueueName=settings.QUEUE_NAME)
    for p in await get_patterns():
        match = re.search(p, text)
        if match:
            await create_message(text, match.group(0))
            client_slack = build_client_Slack()
            response = client_slack.chat_update(channel=channel, text="This message has been blocked", ts=ts, attachments=[], )
            
def send_message_to_SQS(msg_body, ts, channel):
        client = boto3.resource("sqs", region_name=settings.REGION_NAME, aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_KEY_ID)
        queue = client.get_queue_by_name(QueueName=settings.QUEUE_NAME)
        response = queue.send_message(QueueUrl=settings.QUEUE_URL, MessageBody=msg_body,  
                                      MessageAttributes={
                                                        'timestamp': {
                                                            'StringValue': ts,
                                                            'DataType': 'String'
                                                        },
                                                        'channel': {
                                                            'StringValue': channel,
                                                            'DataType': 'String'
                                                        }
                                                    } 
                                                        )



    