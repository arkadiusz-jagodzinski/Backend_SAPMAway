from django.template import loader
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {
        'time': datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
    }
    return HttpResponse(template.render(context, request))
