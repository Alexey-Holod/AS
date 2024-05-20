from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('shop/<int:product_type>', shop, name='shop'),
    path('product_details/<int:produkt_id>', product_details, name='product_details'),

]
