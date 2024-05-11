from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', moder, name='moder'),
    path('brand/', add_brand, name='brand'),
    path('type_product/', type_product, name='type_product'),
    path('age_category/', age_category, name='age_category'),
    path('size/', size, name='size'),
    path('delete/<str:table>/<int:id>', delete, name='delete'),
    path('load_photo/<int:ProductID>', load_photo, name='LoadPhoto')
]