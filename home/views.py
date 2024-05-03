from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    Prod = Product.objects.all()
    # Распихиваем фотки то товарам
    ProdAndPhoto = {}
    for item_prod in Prod:
        ProdAndPhoto[item_prod] = item_prod.images.all()[:4]

    print('****', ProdAndPhoto)
    context = {'ProdAndPhoto': ProdAndPhoto, }
    return render(request, 'home/home.html', context)
