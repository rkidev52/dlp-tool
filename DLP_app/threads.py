import asyncio
import json
from .utils import build_client, search_for_leaks

async def search_leaks(text):
    search_for_leaks(text)


class Manager:

    def __init__(self, queue_name: str):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop = asyncio.get_event_loop()
        self.queue = queue_name
    
    async def _get_messages(self):
        """Read and pop messages from SQS queue
        """
        client = build_client()
        queue = client.get_queue_by_name(QueueName="TestQueue")

        all_messages=[]
        i=1

        while True:
            messages = queue.receive_messages(MaxNumberOfMessages=10)
            for msg in messages:
                all_messages.append(msg.body)
                msg.delete()
            if len(messages) == 0:
                break
        print(all_messages)
        return all_messages

    async def main(self):

        while True:
            messages = await self._get_messages()
            for message in messages:
                
                self.loop.create_task(search_leaks(message))
            await asyncio.sleep(1)
