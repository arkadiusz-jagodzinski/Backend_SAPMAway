from django.shortcuts import render
import json
from django.http import JsonResponse
from .spamcheck import isSpam

# Create your views here.

from django.http import HttpResponse

def index(requests):

	if(requests.method != 'GET'):
		return HttpResponse("Bad method", status=400)

	if(requests.content_type != 'application/json'):
		return HttpResponse("Wrong content type", status=400)

	if(len(requests.body) == 0): 
		return HttpResponse("Empty body", status=400)

	data = json.loads(requests.body)

	if not 'content' in data:
		return HttpResponse("Content not found", status=400)

	content = data['content']

	if(len(content) > 1000):
		return HttpResponse("Message too long", status=400)
		
	if(len(content) == 0):
		return HttpResponse("Message too short", status=400)

	return JsonResponse({'spamPropability': isSpam(content)})
