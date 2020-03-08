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

# Add product page
def add_prodcut(request):
    args = {}
    if request.method == 'POST':
        # new_trainee = EnrollTrainee()
        title = request.POST['product_title']
        print(title)
    return render(request, 'pages/add-product.html', args)