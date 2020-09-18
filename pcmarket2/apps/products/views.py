from django.http import HttpResponse
from .models import *
from django.shortcuts import render
import urllib.request


def index(request):
    return render(request, 'product/processors.html', locals())

