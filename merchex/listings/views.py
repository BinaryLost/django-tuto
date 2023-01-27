# ~/hag/www/django-tuto/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>A propos de nous!</h1>')

def listings(request):
    return HttpResponse('<h1>Listing</h1>')

def contact(request):
    return HttpResponse('<h1>Contact</h1>')
