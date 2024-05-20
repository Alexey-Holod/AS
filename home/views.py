from django.shortcuts import render
from .models import *
from .OtherFunction import *
# Create your views here.

def home(request):
    HomePage = show_product(request)
    ProductTypeList = ProductType.objects.all()
    context = {'ProdAndPhoto': HomePage,
               'ProductTypeList': ProductTypeList}
    return render(request, 'home/home.html', context)


def shop(request, product_type):
    Brends = Brand.objects.all()
    ProdAndPhoto = show_product(request, product_type)
    ProductTypeList = ProductType.objects.all()
    context = {'Brends': Brends, 'ProductTypeList': ProductTypeList,
               'ProdAndPhoto': ProdAndPhoto}
    return render(request, 'home/shop.html', context=context)


def product_details(request, produkt_id):
    ProdDetails = Product.objects.get(id = produkt_id)
    ProdPhoto = ProdDetails.images.all()
    ProdSize = ProdDetails.Product_size.all()
    ProductTypeList = ProductType.objects.all()
    context = {'ProductTypeList': ProductTypeList, 'ProdDetails': ProdDetails, 'ProdPhoto': ProdPhoto, 'ProdSize': ProdSize};
    return render(request, 'home/product-details.html', context)
