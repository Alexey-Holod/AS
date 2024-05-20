from .models import *

def show_product(request, switc=0):
    if switc == 0:
        Prod = Product.objects.all()
    else:
        Prod = Product.objects.filter(Product_type=switc)
    ProdAndPhoto = {}
    for item_prod in Prod:
        ProdAndPhoto[item_prod] = item_prod.images.all()[:4]
    return ProdAndPhoto
