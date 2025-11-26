from django.shortcuts import render, redirect
from delivery.models import ProductDelivery, DeliveryStatus
from django.utils.translation.template import context_re
from home.OtherFunction import check_user_cart, show_product, take_photos
from home.models import Product, ProductType


def user_home(request, user_id):
    User_Deliv = ProductDelivery.objects.filter(Customer = user_id).filter(Name_product = 2)
    context = {'orders': User_Deliv}
    return render(request, 'users/my-account.html', context = context)

# корзина покупателя
# Name_product - Статус доставки
def user_cart(request, flag = 'В_корзине'):
    # Получаем товары с фотками для корзины покупателя
    HomePage = show_product()
    # Если пользователь авторизован, то стоит узнать,
    # какие товары он имеет в корзине и отметить их
    if str(request.user) != 'AnonymousUser':
        # Обработка проверки товаров корзины вынесена в отдельный экспортируемый файл
        # потому то к ней будем обращаться и в других функциях
        if flag == 'Заказанные':
            check_user_cart1 = check_user_cart(request, 2)
        elif flag == 'Куплено':
            check_user_cart1 = check_user_cart(request, 5)
        elif flag == 'Отмена':
            check_user_cart1 = check_user_cart(request, 3)
        else:
            check_user_cart1 = check_user_cart(request)
        #-------------------------------------------------
        CART = []

        for i in check_user_cart1['User_cart']:
            Product = HomePage.get(id = i.ProductID.id)
            CART.append({i:Product})

        #-------------------------------------------------
        ProductTypeList = ProductType.objects.all()
        context = {'ProdAndPhoto': CART,
                   # Получаем типы продуктов для пунктов меню
                   'ProductTypeList': ProductTypeList,
                   # Количество одинаковых товаров в корзине
                   'User_cart': check_user_cart1['U_cart'],
                   # Общее количество товаров в корзине
                   'quantity_of_goods':check_user_cart1['quantity_of_goods'],
                   # Флаг для отрисовки кнопки удаления товара из корзины
                   'cart': True,
                   'select':flag
                   }
    return render(request, 'users/my-account.html', context=context)


def buy(request, order_id, flag):
    User_will_buy = ProductDelivery.objects.get(id = order_id)
    User_will_buy.Name_product = DeliveryStatus.objects.get(id = 2)
    User_will_buy.save()
    Cart = ProductDelivery.objects.filter(Customer=request.user).filter(Name_product=1)
    context = {'orders': Cart}
    if (str(request.user) != 'AnonymousUser'):
        check_user_cart1 = check_user_cart(request)
        # Чтобы показать какие товары уже в корзине и сколько их
        context['User_cart'] = check_user_cart1['U_cart']
        # Показать общее количество товаров в корзине на значке корзины
        context['quantity_of_goods'] = check_user_cart1['quantity_of_goods']
    if flag == 'cart':
        context['label'] = 'user_cart'
    return render(request, 'users/my-account.html', context=context)


def user_cart_del(request, order_id, flag):
    # Удаляем заказ из таблицы заказов
    ProductDelivery.objects.filter(id=order_id).delete()
    return user_cart(request, request.user)
