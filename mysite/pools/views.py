from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hi there General Kenobi..Here are your polls. Make sure you check')
# Create your views here.
