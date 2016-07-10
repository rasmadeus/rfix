from django.http import HttpResponse
from django.template.loader import get_template

def index(request):
    template = get_template('index.html')
    context = {
        'greeting': 'Hello world!'
    }
    return HttpResponse(template.render(context, request))
