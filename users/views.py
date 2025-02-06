from django.shortcuts import render, redirect
from delivery.models import ProductDelivery, DeliveryStatus
from django.utils.translation.template import context_re
from home.OtherFunction import check_user_cart, show_product, take_photos
from home.models import Product


def user_home(request, user_id):
    User_Deliv = ProductDelivery.objects.filter(Customer = user_id).filter(Name_product = 2)
    context = {'orders': User_Deliv}
    return render(request, 'users/my-account.html', context = context)

# корзина покупателя
# Name_product - Статус доставки
def user_cart(request, user_id):
    '''Удали к хуям содержимое этой функции и используй сетку со слайдерами как на страртовой
    с фильтром по корзине покупателя и доп. информацией и таблицы ProductDelivery'''
    Delivery = ProductDelivery.objects.filter(Customer=user_id).filter(Name_product=1)
    ProdAndPhotoInCart = []
    for i in Delivery:
        ProdAndPhotoInCart.append(i.ProductID) # Почему-то не удается получить фотки. Надо допилить!


    ProdCartImage = Product.objects.filter(id = ProdAndPhotoInCart[0].id)
    print('---y2e---', len(ProdCartImage))

    # передаю в шаблон переменную 'label':'user_cart' для отрисовки кнопки-значек корзина
    context = {'orders': Delivery, 'label':'user_cart'}
    # Получаем фотки для слайдеров
    # Обработка проверки товаров корзины
    if (str(request.user) != 'AnonymousUser'):
        check_user_cart1 = check_user_cart(request)
        # Чтобы показать какие товары уже в корзине и сколько их
        context['User_cart'] = check_user_cart1['U_cart']

        context['ProdAndPhotoInCart'] = ProdAndPhotoInCart
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
