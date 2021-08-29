from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def function1(request):
    return HttpResponse('This is my first Django view')

def welcome(request,name):
    return HttpResponse(f'Hello My Friend {name}')