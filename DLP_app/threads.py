import asyncio
import json
from .utils import build_client_SQS, search_for_leaks

async def search_leaks(text, channel, ts):
    await search_for_leaks(text, channel, ts)


class Manager:

    def __init__(self, queue_name: str):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        # self.loop = asyncio.get_event_loop()
        self.queue = queue_name
    
    
    async def _get_messages(self):
        """Read and pop messages from SQS queue
        """
        client = build_client_SQS()
        queue = client.get_queue_by_name(QueueName="TestQueue")

        all_messages=[]
        i=1

        while True:
            messages = queue.receive_messages(MaxNumberOfMessages=10, MessageAttributeNames=['All'])
            for msg in messages:
                msg_dict = dict()
                msg_dict["body"]=msg.body
                msg_dict["attributes"]=msg.message_attributes
                all_messages.append(msg_dict)
                msg.delete()
            if len(messages) == 0:
                break
        print(all_messages)
        return all_messages

    async def main(self):
        while True:
            messages = await self._get_messages()
            for message in messages:
                task = asyncio.create_task(search_leaks(message["body"], message["attributes"].get("channel").get("StringValue"), message["attributes"].get("timestamp").get("StringValue")))
                await task
            await asyncio.sleep(1)