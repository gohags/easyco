from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def hello_world(request):

    space = os.environ.get('SPACE','World')
    html = "<html><body>Hello {}!</body></html>".format(space)
    return HttpResponse(html)