from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
from django.http import HttpResponse, JsonResponse
import slack
import requests
import re
from .models import Message
from .utils import search_for_leaks, send_message_to_SQS, build_client_SQS
import boto3
from .threads import Manager
import asyncio
# Create your views here.

def indexView(request):
    return render(request, 'index.html')

def SearchPatternsView(request):
    manager = Manager(settings.QUEUE_URL)
    asyncio.run(manager.main())
    return HttpResponse("all msgs searched")


@csrf_exempt
def event_hook(request):
    client = slack.WebClient(token=settings.BOT_USER_ACCESS_TOKEN)
    json_dict = json.loads(request.body.decode('utf-8'))
    if json_dict['token'] != settings.VERIFICATION_TOKEN:
        return HttpResponse(status=403)
    if 'type' in json_dict:
        if json_dict['type'] == 'url_verification':
            response_dict = {"challenge": json_dict['challenge']}
            return JsonResponse(response_dict, safe=False)
    if 'event' in json_dict:
        event_msg = json_dict['event']
        if event_msg['type'] == 'message':
            if "files" in event_msg:
                send_message_to_SQS(event_msg["files"][0]["preview"],event_msg["ts"], event_msg["channel"])
                return HttpResponse(status=201)
            elif "text" in event_msg:
                try:
                    send_message_to_SQS(event_msg["text"],event_msg["ts"], event_msg["channel"])
                except Exception as e:
                    print(e)
            elif "files" and "text" in event_msg:
                send_message_to_SQS(event_msg["text"])
                send_message_to_SQS(event_msg["files"][0]["preview"],event_msg["ts"], event_msg["channel"])
    return HttpResponse(status=200)
