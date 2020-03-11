from django.contrib import admin
from .models import *

admin.site.site_header = 'Admin'

admin.site.register(Product)
