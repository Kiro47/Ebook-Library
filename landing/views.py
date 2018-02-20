from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):

    #template = loader.get_template('landing/template')

    return render(request, 'landing/templates/landing/index.html')

    #return HttpResponse("Landing Page")