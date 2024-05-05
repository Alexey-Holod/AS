from django.contrib import admin
from django.urls import path
from  .views import *

urlpatterns = [
    path('', home, name='home'),
    path('product_details/<int:produkt_id>', product_details, name='product_details'),

]
