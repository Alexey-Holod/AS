from django.shortcuts import render, redirect
import datetime
from home.models import Product, Size
from django.contrib.auth.models import User
from .models import ProductDelivery, DeliveryStatus


def add_to_cart(request, id_product, id_size):
    print('--------------req--------------\n', id_size)
    if str(request.user) == 'AnonymousUser':
        return redirect('auth_user_do')
    GetProduct = Product.objects.get(id = id_product)
    P_D = ProductDelivery()
    DelStatus = DeliveryStatus.objects.get(id = 1)
    P_D.Customer = User.objects.get(id = request.user.id)
    P_D.ClientName = request.user
    P_D.ProductID = GetProduct
    P_D.Name_product = DelStatus
    P_D.ClientAddres = 'addres'
    P_D.ClientPhone = '88005553535'
    P_D.ClientMAil = 'Mail'
    P_D.date = datetime.datetime.now().strftime("%Y%m%d")
    P_D.ProductSize = Size.objects.get(id = id_size)

    P_D.save()
    return redirect('home')
