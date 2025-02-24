from django.shortcuts import render, redirect
import datetime
from home.models import Product, Size
from home.views import product_details
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
    P_D.ClientMAil = User.objects.get(id = request.user.id)
    P_D.date = datetime.datetime.now().strftime("%Y%m%d")
    P_D.ProductSize = Size.objects.get(id = id_size)

    P_D.save()
    return redirect('home')

def order(request, id_product, id_size, ):
    # Получаем объект размера что-бы использовать его при поиске
    size = Size.objects.get(size_range=id_size)
    # Делаю поиск в таблице ProductDelivery с помощью двух параметров
    ProdDeliVOrder = ProductDelivery.objects.filter(ProductID = id_product).filter(ProductSize = size)
    # Т.к. при запросе выше мы получили обект "Набор", то используя его запросим один конкретный объект
    Here = ProductDelivery.objects.get(id = ProdDeliVOrder[0].id)
    # Далее запросим объект статуса заказа который нам нужен "ЗАКАЗАН"
    DevStatus = DeliveryStatus.objects.get(id = 2)
    # Теперь присваиваем свойству объекта заказа новый статус
    Here.Name_product = DevStatus
    # Сохраняем
    Here.save()
    return product_details(request, id_product, id_size, 'disable_size')