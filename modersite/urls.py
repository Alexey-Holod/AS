from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', moder, name='moder'),
    path('brand/', add_brand, name='brand'),
    path('type_product/', type_product, name='type_product'),
    path('age_category/', age_category, name='age_category'),
    path('size/', size, name='size'),
    path('textile/', textile, name='textile'),
    path('delete/<str:table>/<int:id>', delete, name='delete'),
    path('load_photo/<int:ProductID>', load_photo, name='LoadPhoto'),
    path('edit_product/<int:prod_id>', edit_product, name='edit_product'),
    path('delete_product/<int:prod_id>', delete_product, name='delete_product'),
    path('delete_one_photo/<int:prod_id>/<int:id_photo>', delete_one_photo, name='delete_one_photo')
]
