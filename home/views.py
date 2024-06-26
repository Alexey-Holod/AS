from django.shortcuts import render, redirect
from .models import *
from  .forms import *
from .OtherFunction import *
# Create your views here.


def home(request):
    HomePage = show_product(request)
    ProductTypeList = ProductType.objects.all()
    context = {'ProdAndPhoto': HomePage,
               'ProductTypeList': ProductTypeList}
    return render(request, 'home/home.html', context)


def shop(request, product_type, gender):
    Brends = Brand.objects.all()
    IDGen = Gender.objects.get(gender_name=gender)
    ProdAndPhoto = show_product(request, product_type, [], IDGen.id)
    ProductTypeList = ProductType.objects.all()
    price_form = PriceFormSearch
    AgeRange = AgeCategory.objects.all()
    context = {'Product_age_category': '00-00', 'Brends': Brends, 'ProductTypeList': ProductTypeList,
               'ProdAndPhoto': ProdAndPhoto, 'find_price_form': price_form, 'AgeRange': AgeRange,
               'product_type': product_type, 'gender': gender}
    return render(request, 'home/shop.html', context=context)


def find_price_form(request, product_type, gender, Product_age_category):
    IDGen = Gender.objects.get(gender_name=gender)
    if request.method == "POST":
        # Создаем объект формы с данными
        price_form = PriceFormSearch(request.POST)
        if price_form.is_valid():
            # Распихиваем очищенные данные по переменным
            price_from = price_form.cleaned_data['price_from']
            price_to = price_form.cleaned_data['price_to']
            price_Product_age_category = price_form.cleaned_data['Product_age_category']
            print('000000000000000000000000000000000000000000000000', price_Product_age_category)
            # Функция show_product вернет результат поиска
            ProductObj = show_product(request, product_type, [price_from, price_to], IDGen.id, price_Product_age_category)
            ProductTypeList = ProductType.objects.all()
            context = {'Product_age_category': price_Product_age_category, 'ProdAndPhoto': ProductObj, 'ProductTypeList': ProductTypeList,
                       'product_type': product_type, 'find_price_form': price_form,
                       'gender': gender}
            return render(request, 'home/shop.html', context=context)
        else:
            price_form.add_error(None, 'form1 Ошибка добавления бренда')
    else:
        return redirect('home')


def product_details(request, produkt_id):
    ProdDetails = Product.objects.get(id=produkt_id)
    ProdPhoto = ProdDetails.images.all()
    ProdSize = ProdDetails.Product_size.all()
    ProductTypeList = ProductType.objects.all()
    context = {'ProductTypeList': ProductTypeList, 'ProdDetails': ProdDetails,
               'ProdPhoto': ProdPhoto, 'ProdSize': ProdSize};
    return render(request, 'home/product-details.html', context)
