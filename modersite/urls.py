from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', moder, name='moder'),
    path('load_photo/<int:ProductID>', load_photo, name='LoadPhoto')
]