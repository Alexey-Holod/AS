from django.shortcuts import render, redirect
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
            ProductObj.Product_size.set(request.POST.getlist('Product_size'))
            FormAddPhotoProduct = AddPhotoProduct
            return render(request, 'modersite/add_photo_product.html',
                          {'FormAddPhotoProduct': FormAddPhotoProduct, 'title': 'Добавить фото товара',
                           'ProductID': ProductObj.id})
        else:
            FormAddProduct.add_error(None, 'form1 Ошибка добавления лота')
    FormAddProduct = AddProduct
    FormAddBrand = AddBrand
    FormAddProductType = AddProductType
    FormAddAgeCategory = AddAgeCategory
    FormAddSize = AddSize
    ProdType = ProductType.objects.all()
    Brands = Brand.objects.all()
    AgeCategories = AgeCategory.objects.all()
    Sizes = Size.objects.all()
    print('*******************', type(Brands))
    context = {'FormAddProduct': FormAddProduct,
               'FormAddBrand': FormAddBrand,
               'FormAddProductType':FormAddProductType,
               'FormAddAgeCategory': FormAddAgeCategory,
               'FormAddSize': FormAddSize,
               'Brands': Brands,
               'ProdType': ProdType,
               'AgeCategories': AgeCategories,
               'Sizes': Sizes}
    return render(request, 'modersite/moder.html', context=context)


def add_brand(request):
    if request.method == "POST":
        FormAddBrand = AddBrand(request.POST)
        if FormAddBrand.is_valid():
            BrandtObj = FormAddBrand.save(commit=False)
            BrandtObj.save()
            return redirect('moder')
        else:
            FormAddBrand.add_error(None, 'form1 Ошибка добавления бренда')
    return redirect('moder')


def type_product(request):
    if request.method == "POST":
        FormAddProductType = AddProductType(request.POST)
        if FormAddProductType.is_valid():
            ProductTypeObj = FormAddProductType.save(commit=False)
            ProductTypeObj.save()
            return redirect('moder')
        else:
            FormAddProductType.add_error(None, 'form1 Ошибка добавления бренда')
    return redirect('moder')


def age_category(request):
    if request.method == "POST":
        FormAddAgeCategory = AddAgeCategory(request.POST)
        if FormAddAgeCategory.is_valid():
            AddAgeCategoryObj = FormAddAgeCategory.save(commit=False)
            AddAgeCategoryObj.save()
            return redirect('moder')
        else:
            FormAddAgeCategory.add_error(None, 'form1 Ошибка добавления бренда')
    return redirect('moder')


def size(request):
    if request.method == "POST":
        FormAddSize = AddSize(request.POST)
        if FormAddSize.is_valid():
            SizeObj = FormAddSize.save(commit=False)
            SizeObj.save()
            return redirect('moder')
        else:
            FormAddSize.add_error(None, 'form1 Ошибка добавления бренда')
    return redirect('moder')

def delete(request, table, id):
    if table == 'Size':
        Size.objects.filter(id=id).delete()
    elif table == 'AgeCategories':
        AgeCategory.objects.filter(id=id).delete()
    elif table == 'ProdType':
        ProductType.objects.filter(id=id).delete()
    elif table == 'Brands':
        Brand.objects.filter(id=id).delete()
    else:
        ErrMess = 'Не удалось определить модель или атрибут =( '
    return redirect('moder')

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
