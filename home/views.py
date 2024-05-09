from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    Prod = Product.objects.all()
    # Распихиваем фотки то товарам
    ProdAndPhoto = {}
    for item_prod in Prod:
        ProdAndPhoto[item_prod] = item_prod.images.all()[:4]
    context = {'ProdAndPhoto': ProdAndPhoto, }
    return render(request, 'home/home.html', context)

def product_details(request, produkt_id):
    ProdDetails = Product.objects.get(id = produkt_id)
    ProdPhoto = ProdDetails.images.all()
    ProdSize = ProdDetails.Product_size.all()
    print('**********', ProdDetails)
    print('**********', ProdSize)
    context = {'ProdDetails': ProdDetails, 'ProdPhoto': ProdPhoto, 'ProdSize': ProdSize};
    return render(request, 'home/product-details.html', context)
