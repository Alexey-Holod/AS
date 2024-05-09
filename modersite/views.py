from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from home.models import *


def moder(request):
    if request.method == "POST":
        FormAddProduct = AddProduct(request.POST)
        print('________0_______', request.POST)
        testmy = request.POST.getlist('Product_size')
        print('________1_______', testmy)
        if FormAddProduct.is_valid():
            try:
                ProductObj = FormAddProduct.save(commit=False)
                print('1 - OK')
                Article = (str(ProductObj.Product_brand.id) + '.' + str(ProductObj.Product_type.id) + '.' +
                           str(ProductObj.Product_type.id) + '.' + str(ProductObj.Product_gender.id))
                print('2 - OK')
                ProductObj.Posted_by = request.user
                print('3 - OK')
                ProductObj.Product_code = Article
                print('4 - OK')
                ProductObj.save()

                ProductObj.Product_size.set(request.POST.getlist('Product_size'))
                print('/-----/')
                print('5 - OK')
                FormAddPhotoProduct = AddPhotoProduct
            except:
                #FormAddProduct = AddProduct
                return render(request, 'modersite/moder.html',
                              {'FormAddProduct': FormAddProduct,
                               'title': 'Добавить товара'})
            return render(request, 'modersite/add_photo_product.html',
                          {'FormAddPhotoProduct': FormAddPhotoProduct, 'title': 'Добавить фото товара',
                           'ProductID': ProductObj.id})
        else:
            print('________3_______', FormAddProduct.is_valid())
            FormAddProduct.add_error(None, 'form1 Ошибка добавления лота')
    FormAddProduct = AddProduct
    context = {'FormAddProduct': FormAddProduct}
    return render(request, 'modersite/moder.html', context=context)


def load_photo(request, ProductID):
    if request.method == "POST":
        FormAddPhotoProduct = AddPhotoProduct(request.POST, request.FILES)
        if FormAddPhotoProduct.is_valid():
            try:
                loading = FormAddPhotoProduct.save(commit=False)
                ProductLink = Product.objects.get(id=ProductID)
                loading.Product_link = ProductLink
                loading.save()
            except:
                FormAddPhotoProduct.add_error(None, 'form1 Ошибка добавления фото')
    else:
        FormAddPhotoProduct = AddPhotoProduct()
    PhotoOneProduct = PhotoProduct.objects.filter(Product_link=ProductID)
    context = {'FormAddPhotoProduct': FormAddPhotoProduct, 'title': 'Добавить фото', 'PhotoOneProduct': PhotoOneProduct, 'ProductID':ProductID}
    return render(request, 'modersite/add_photo_product.html', context=context)
