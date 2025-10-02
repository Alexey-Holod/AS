from .models import *
from delivery.models import ProductDelivery

def check_gender(Prod, gender):
    if gender == 2:
        Prod = Prod.exclude(Product_gender=3)
    else:
        Prod = Prod.exclude(Product_gender=2)
    return Prod

def take_photos(Prod):
    ProdAndPhoto = {}
    for item_prod in Prod:
        ProdAndPhoto[item_prod] = item_prod.images.all()[:4]
    return ProdAndPhoto

def show_product(product_type=0, rang_price=[], gender='', age='None',):
    if product_type == 0 and len(rang_price) == 0:
        Prod = Product.objects.all()
    elif len(rang_price) == 2:
        # Если возраст не "пустой" то ищем с учетом возраста
        if age != None:
            Prod = Product.objects.filter(Product_age_category=age).filter(Product_type=product_type)
        # Если возраст пустой то ищем только по цене и гендеру
        elif age == None:
            Prod = Product.objects.filter(Product_type=product_type)
        Prod = check_gender(Prod, gender)
        # Убираем товары не попавшие в возростной диапазон
        for pd in Prod:
            if (int(pd.Product_price) < int(rang_price[0])) or (int(pd.Product_price) > int(rang_price[1])):
                Prod = Prod.exclude(id=pd.id)
    else:
        Prod = Product.objects.filter(Product_type=product_type)
        Prod = check_gender(Prod, gender)
    ProdAndPhoto = take_photos(Prod)
    return ProdAndPhoto

# Проверяем корзину, показываем какие товары в корзине и сколько их
def check_user_cart(request, DelStat=1):
    if request.user.is_superuser:
        User_cart = ProductDelivery.objects.filter(Name_product=DelStat)
    else:
        # Получаем все заказы пользователя
        All_User_cart = ProductDelivery.objects.filter(Customer=request.user.id)
        # Теперь получаем наборы разделенные по статусам
        Ordered = All_User_cart.filter(Name_product=2)
        Purchased = All_User_cart.filter(Name_product=5)
        Cancelled = All_User_cart.filter(Name_product=3)
        # Отсортируем те которые выбраны в соответствии со статусом заказа
        User_cart = All_User_cart.filter(Name_product=DelStat)
        # User_cart = ProductDelivery.objects.filter(Customer=request.user.id).filter(Name_product=DelStat)

    U_cart = {}
    for i in User_cart:
        if i.ProductID in U_cart:
            U_cart[i.ProductID] += 1
        else:
            U_cart[i.ProductID] = 1
    # Передаю товары которые в корзине через User_cart
    return {'User_cart': User_cart, 'U_cart': U_cart,
            'quantity_of_goods': len(User_cart), 'Sum_Ordered':len(Ordered),
            'Sum_Purchased':len(Purchased), 'Sum_Cancelled':len(Cancelled)}
