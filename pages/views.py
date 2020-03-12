from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
import urllib.parse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Test page
def t(request):
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'pages/t.html', {'uploaded_file_url': uploaded_file_url})
    else:
        return render(request, 'pages/t.html')

# Home page
def pages(request):
    args = {}
    all_products = Product.objects.all()
    args['products'] = all_products
    return render(request, 'pages/index.html', args)

# Product page
def product(request):
    args = {}
    return render(request, 'pages/product.html', args)

# Product page
def product_detail(request, pk):
    product = Product.objects.all().filter(pk=pk)[0]
    similar_products = Product.objects.all()[0:4]
    print(similar_products)
    args = {'product': product, 'similar_products':similar_products}
    return render(request, 'pages/product.html', args)

# Add product page
def add_prodcut(request):
    args = {}
    if request.method == 'POST':
        myfile = request.FILES['product_image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        new_product = Product()
        new_product.title = request.POST['product_title']
        new_product.price = request.POST['price']
        new_product.description = request.POST['description']
        new_product.product_image = uploaded_file_url
        new_product.save()
    return render(request, 'pages/add-product.html', args)

