from django.shortcuts import render
import json
from django.http import JsonResponse
from .spamcheck import isSpam

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Sms

# Disable CSRF protection
# https://docs.djangoproject.com/en/3.0/ref/csrf/
@csrf_exempt
def index(requests):

	if(requests.method != 'POST'):
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

	isspam = isSpam(content)
	sms = Sms(spamProbability = isspam, content = content)
	sms.save()
	
	return JsonResponse({'spamPropability': isspam})

