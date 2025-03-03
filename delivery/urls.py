from django.urls import path
from .views import *

urlpatterns = [
    path('add_to_cart/<int:id_product>/<int:id_size>', add_to_cart, name='add_to_cart'),
path('order/<int:id_product>/<slug:id_size>', order, name='order'),
    path('order/<int:id_product>/<slug:id_size>/<str:status>', order, name='order'),
]
