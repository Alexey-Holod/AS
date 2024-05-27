from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('shop/<int:product_type>', shop, name='shop'),



    path('find_price_form/<int:product_type>', find_price_form, name='find_price_form'),



    path('product_details/<int:produkt_id>', product_details, name='product_details'),
]
