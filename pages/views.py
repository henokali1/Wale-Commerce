from django.views.generic import TemplateView
from django.shortcuts import render
from .models import *
import urllib.parse

# Home page
def pages(request):
	return render(request, 'pages/index.html')

# Product page
def product(request):
    args = {}
    return render(request, 'pages/product.html', args)