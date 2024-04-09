from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from home.models import *


def moder(request):
    if request.method == "POST":
        FormAddProduct = AddProduct(request.POST)
        if FormAddProduct.is_valid():
            ProductObj = FormAddProduct.save(commit=False)
            Article = (str(ProductObj.Product_brand.id) + '.' + str(ProductObj.Product_type.id) + '.' +
                       str(ProductObj.Product_type.id) + '.' + str(ProductObj.Product_gender.id))
            ProductObj.Posted_by = request.user
            ProductObj.Product_code = Article
            ProductObj.save()
            FormAddPhotoProduct = AddPhotoProduct
            return render(request, 'modersite/add_photo_product.html',
                          {'FormAddPhotoProduct': FormAddPhotoProduct, 'title': 'Добавить фото товара',
                           'ProductID': ProductObj.id})
        else:
            FormAddProduct.add_error(None, 'form1 Ошибка добавления лота')
    FormAddProduct = AddProduct
    return render(request, 'modersite/moder.html', {'FormAddProduct': FormAddProduct})


def load_photo(request, ProductID):
    print('ХУЙ1')
    if request.method == "POST":
        print('ХУЙ2')
        FormAddPhotoProduct = AddPhotoProduct(request.POST, request.FILES)
        if FormAddPhotoProduct.is_valid():
            print('ХУЙ3')
            try:
                loading = FormAddPhotoProduct.save(commit=False)
                ProductLink = Product.objects.get(id=ProductID)
                loading.Product_link = ProductLink
                loading.save()
            except:
                print('ХУЙ4')
                FormAddPhotoProduct.add_error(None, 'form1 Ошибка добавления фото')
        else:
            print('ХУЙ ТАМ ПЛАВАЛ!')
    else:
        FormAddPhotoProduct = AddPhotoProduct()
    PhotoOneProduct = PhotoProduct.objects.filter(Product_link=ProductID)
    context = {'FormAddPhotoProduct': FormAddPhotoProduct, 'title': 'Добавить фото', 'PhotoOneProduct': PhotoOneProduct, 'ProductID':ProductID}
    return render(request, 'modersite/add_photo_product.html', context=context)
