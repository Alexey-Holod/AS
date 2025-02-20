from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .OtherFunction import show_product, check_user_cart
from delivery.models import ProductDelivery


def home(request):
    # Получаем товары с фотками для главной страници
    HomePage = show_product()
    ProductTypeList = ProductType.objects.all()
    context = {'ProdAndPhoto': HomePage,
               'ProductTypeList': ProductTypeList}
    # Если пользователь авторизован, то стоит узнать,
    # какие товары он имеет в корзине и отметить их
    if (str(request.user) != 'AnonymousUser'):
        # Обработка проверки товаров корзины вынесена в отдельный экспортируемый файл
        # потому то к ней будем обращаться и в других функциях и даже модулях
        check_user_cart1 = check_user_cart(request)
        # Чтобы показать какие товары уже в корзине и сколько их
        context['User_cart'] = check_user_cart1['U_cart']
        # Показать общее количество товаров в корзине на значке корзины
        context['quantity_of_goods'] = check_user_cart1['quantity_of_goods']
    return render(request, 'home/home.html', context)


def shop(request, product_type, gender):
    Brends = Brand.objects.all()
    IDGen = Gender.objects.get(gender_name=gender)
    ProdAndPhoto = show_product(product_type, [], IDGen.id)
    ProductTypeList = ProductType.objects.all()
    price_form = PriceFormSearch
    AgeRange = AgeCategory.objects.all()
    context = {'Product_age_category': '00-00',
               'Brends': Brends,
               'ProductTypeList': ProductTypeList,
               'ProdAndPhoto': ProdAndPhoto,
               'find_price_form': price_form,
               'AgeRange': AgeRange,
               'product_type': product_type,
               'gender': gender}
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
            # Функция show_product вернет результат поиска
            ProductObj = show_product(product_type, [price_from, price_to], IDGen.id, price_Product_age_category)
            ProductTypeList = ProductType.objects.all()
            context = {'Product_age_category': price_Product_age_category,
                       'ProdAndPhoto': ProductObj,
                       'ProductTypeList': ProductTypeList,
                       'product_type': product_type,
                       'find_price_form': price_form,
                       'gender': gender,
                       # Для того чтобы отобразить возрастную категорию
                       'age_category': price_Product_age_category}
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
    context = {'ProductTypeList': ProductTypeList,
               'ProdDetails': ProdDetails,
               'ProdPhoto': ProdPhoto,
               'ProdSize': ProdSize};
    return render(request, 'home/product-details.html', context)
