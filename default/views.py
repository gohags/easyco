from django.shortcuts import render
from django.http import HttpResponse
import os
import json

# Create your views here.
def hello_world(request):

    space = os.environ.get('SPACE',"""\{\}""")
    space = json.loads(space)
    html = "<html><body>Hello {}!</body></html>".format(space['SPACE'])
    return HttpResponse(html)