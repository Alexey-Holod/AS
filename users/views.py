from django.shortcuts import render, redirect
from delivery.models import ProductDelivery, DeliveryStatus
from django.utils.translation.template import context_re
from home.OtherFunction import check_user_cart, show_product
from home.models import Product


def user_home(request, user_id):
    User_Deliv = ProductDelivery.objects.filter(Customer = user_id).filter(Name_product = 2)
    context = {'orders': User_Deliv}
    return render(request, 'users/my-account.html', context = context)

# корзина покупателя
def user_cart(request, user_id):

    Cart = ProductDelivery.objects.filter(Customer=user_id).filter(Name_product=1)
    ID_Prod = []
    for i in Cart:
        ID_Prod.append(i.ProductID)
    print('---ye---', ID_Prod)
    ProdCartImage = Product.objects.filter(id = ID_Prod[0])
    print('---ye---', ProdCartImage)

    # передаю в шаблон переменную 'label':'user_cart' для отрисовки кнопки-значек корзина
    context = {'orders': Cart, 'label':'user_cart'}
    # Обработка проверки товаров корзины
    if (str(request.user) != 'AnonymousUser'):
        check_user_cart1 = check_user_cart(request)
        # Чтобы показать какие товары уже в корзине и сколько их
        context['User_cart'] = check_user_cart1['U_cart']
        # Показать общее количество товаров в корзине на значке корзины
        context['quantity_of_goods'] = check_user_cart1['quantity_of_goods']
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
    ProductDelivery.objects.filter(id=order_id).delete()
    context = {}
    if flag == 'cart':
        context['label'] = 'user_cart'
        Cart = ProductDelivery.objects.filter(Customer=request.user).filter(Name_product=1)
    elif flag == 'orders':
        Cart = ProductDelivery.objects.filter(Customer=request.user).filter(Name_product=2)
    context['orders'] = Cart
    if (str(request.user) != 'AnonymousUser'):
        check_user_cart1 = check_user_cart(request)
        # Чтобы показать какие товары уже в корзине и сколько их
        context['User_cart'] = check_user_cart1['U_cart']
        # Показать общее количество товаров в корзине на значке корзины
        context['quantity_of_goods'] = check_user_cart1['quantity_of_goods']
    return render(request, 'users/my-account.html', context=context)
