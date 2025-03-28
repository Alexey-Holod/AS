from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('shop/<int:product_type>/<str:gender>', shop, name='shop'),
    path('find_price_form/<int:product_type>/<str:gender>/<slug:Product_age_category>', find_price_form, name='find_price_form'),
    path('product_details/<int:produkt_id>/<slug:size>/<slug:flag>', product_details, name='product_details'),
]
