from django.urls import path
from . import views


urlpatterns = [
    path('', views.pages, name='index.html'),
    # path('cats/<str:cat_urls>/', views.cat_urls, name='cat_urls.html'),
]