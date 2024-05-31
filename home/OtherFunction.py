from .models import *


def check_gender(Prod, gender):
    if gender == 2:
        Prod = Prod.exclude(Product_gender=3)
    else:
        Prod = Prod.exclude(Product_gender=2)
    return Prod

def show_product(request, switc=0, rang_price=[], gender=''):
    print('---------------', gender)
    if switc == 0 and len(rang_price) == 0:
        Prod = Product.objects.all()
    elif len(rang_price) == 2:
        Prod = Product.objects.filter(Product_type=switc)
        Prod = check_gender(Prod, gender)
        for pd in Prod:
            print('---------------', gender)
            if (int(pd.Product_price) < int(rang_price[0])) or (int(pd.Product_price) > int(rang_price[1])):
                Prod = Prod.exclude(id=pd.id)
    else:
        Prod = Product.objects.filter(Product_type=switc)
        Prod = check_gender(Prod, gender)
    ProdAndPhoto = {}
    for item_prod in Prod:
        ProdAndPhoto[item_prod] = item_prod.images.all()[:4]
    return ProdAndPhoto
