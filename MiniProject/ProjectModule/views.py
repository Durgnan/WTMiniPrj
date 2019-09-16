from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    template = loader.get_template('ProjectModule/index.html')
    return HttpResponse(template.render())
def about(request):
    template = loader.get_template('ProjectModule/about.html')
    return HttpResponse(template.render())