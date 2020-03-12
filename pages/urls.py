from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.pages, name='index.html'),
    path('product/', views.product, name='product.html'),
    path('t/', views.t, name='t.html'),
    path('add-product/', views.add_prodcut, name='add-product.html'),
    path('product/<int:pk>/', views.product_detail, name='product.html'),
    # path('cats/<str:cat_urls>/', views.cat_urls, name='cat_urls.html'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)