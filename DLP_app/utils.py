import re
from .models import Message, Pattern
from django.conf import settings
import boto3
   
def build_client():
    client = boto3.resource(
        "sqs",
        region_name=settings.REGION_NAME,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_KEY_ID
    )
    return client

def search_for_leaks(text):
    client = build_client()
    queue = client.get_queue_by_name(QueueName="TestQueue")
    patterns = list(Pattern.objects.all().values_list("pattern", flat=True).distinct())

    for p in patterns:
        match = re.search(p, text)
        if match:
            # client.chat_postMessage(channel=event_msg['channel'], text="message was blicked")
            message = Message.objects.create(content=text, pattern=match.group(0))


def send_message_to_SQS(msg_body, id):
        client = boto3.resource(
            "sqs",
            region_name=settings.REGION_NAME,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_KEY_ID
        )
        queue = client.get_queue_by_name(QueueName=settings.QUEUE_NAME)
        response = queue.send_message(
            QueueUrl=settings.QUEUE_URL,
            MessageBody=msg_body,
          MessageAttributes={'Author': {'StringValue': id,'DataType': 'String'}}
        )
