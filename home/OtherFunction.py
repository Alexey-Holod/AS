from .models import *


def show_product(request, switc=0, rang_price=[]):
    if switc == 0 and len(rang_price) == 0:
        Prod = Product.objects.all()
    elif len(rang_price) != 0:
        Prod = Product.objects.filter(Product_type=switc)
        for pd in Prod:
            print('---------------', )
            if (int(pd.Product_price) < int(rang_price[0])) or (int(pd.Product_price) > int(rang_price[1])):
                Prod = Prod.exclude(id=pd.id)
    else:
        Prod = Product.objects.filter(Product_type=switc)
    ProdAndPhoto = {}
    for item_prod in Prod:
        ProdAndPhoto[item_prod] = item_prod.images.all()[:4]
    return ProdAndPhoto
