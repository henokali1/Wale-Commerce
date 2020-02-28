from django.views.generic import TemplateView
from django.shortcuts import render
from .models import *
import urllib.parse


def pages(request):
	return render(request, 'pages/index.html')