from .models import *
from delivery.models import ProductDelivery

def check_gender(Prod, gender):
    if gender == 2:
        Prod = Prod.exclude(Product_gender=3)
    else:
        Prod = Prod.exclude(Product_gender=2)
    return Prod


def show_product(request, product_type=0, rang_price=[], gender='', age='None',):
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
        for pd in Prod:
            if (int(pd.Product_price) < int(rang_price[0])) or (int(pd.Product_price) > int(rang_price[1])):
                Prod = Prod.exclude(id=pd.id)
    else:
        Prod = Product.objects.filter(Product_type=product_type)
        Prod = check_gender(Prod, gender)
    ProdAndPhoto = {}
    for item_prod in Prod:
        ProdAndPhoto[item_prod] = item_prod.images.all()[:4]
    return ProdAndPhoto

# Проверяем корзину, показываем какие товары в корзине и сколько их
def check_user_cart(request, ):
    print('USER ----0---- ', request.user)
    User_cart = ProductDelivery.objects.filter(Customer=request.user.id).filter(Name_product=1)
    U_cart = {}
    How_many_pieces = 0
    for i in User_cart:
        if i.ProductID in U_cart:
            How_many_pieces += 1
        else:
            How_many_pieces = 1
        print('-----*-----', U_cart)
        U_cart[i.ProductID] = How_many_pieces
    return {'U_cart': U_cart, 'quantity_of_goods': len(User_cart)}
