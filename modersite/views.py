from django.shortcuts import render, redirect
from .forms import *
from home.OtherFunction import *
from home.models import *
from delivery.models import ProductDelivery, DeliveryStatus
from home.OtherFunction import show_product
from home.OtherFunction import check_user_cart


def order_completed(request, order_id, status):
    status = DeliveryStatus.objects.get(id = status)

    ChangeOrderStatus = ProductDelivery.objects.get(id = order_id)
    ChangeOrderStatus.Name_product = status
    ChangeOrderStatus.save()
    # Если статус "Заказан", то надо вернуться к исполненным заказам
    if str(status) == 'Заказан':
        print('---status---', status)
        return orders(request, 5)
    else:
        return orders(request)


def orders(request, status=2):
    # Получаем товары с фотками для корзины покупателя
    HomePage = show_product()
    # Если пользователь авторизован, то стоит узнать,
    # какие товары он имеет в корзине и отметить их
    print('НЕТ')
    if str(request.user) != 'AnonymousUser':
        print('ДА')
        # Обработка проверки товаров корзины вынесена в отдельный экспортируемый файл
        # потому то к ней будем обращаться и в других функциях и даже модулях
        check_user_cart1 = check_user_cart(request, status)
        CART = []
        print('--=================================--', check_user_cart1)
        for i in check_user_cart1['User_cart']:
            CART.append({i: HomePage[i.ProductID]})
        ProductTypeList = ProductType.objects.all()

        context = {'ProdAndPhoto': CART,
                   # Получаем типы продуктов для пунктов меню
                   'ProductTypeList': ProductTypeList,
                   # Количество одинаковых товаров в корзине
                   'User_cart': check_user_cart1['U_cart'],
                   # Общее количество товаров в корзине
                   'quantity_of_goods': check_user_cart1['quantity_of_goods'],
                   # Флаг для отрисовки кнопки удаления товара из корзины
                   'cart': True}
        if status == 5:
            context['status'] = status
    return render(request, 'modersite/orders.html', context = context)


def moder(request):
    if request.user.id == None or request.user.is_staff == False:
        return redirect('home')
    chekform = False
    ShoweProduct = show_product()
    ProductTypeList = ProductType.objects.all()
    if request.method == "POST":
        FormAddProduct = AddProduct(request.POST)
        if FormAddProduct.is_valid():
            ProductObj = FormAddProduct.save(commit=False)
            FormAddPhotoProduct = AddPhotoProduct
            try:
                Article = (str(ProductObj.Product_brand.id) + '.' + str(ProductObj.Product_type.id) + '.' +
                               str(ProductObj.Product_type.id) + '.' + str(ProductObj.Product_gender.id))
                ProductObj.Posted_by = request.user
                ProductObj.Product_code = Article
                ProductObj.save()
                #PhotoOneProduct = ProductObj.images.all()
                ProductObj.Product_size.set(request.POST.getlist('Product_size'))
            except:
                # Если возникла ошибка значит не все поля были заполнены
                # Ставим флаг в значение TRUE и передаем на форму, там разберуться что с этим делать...
                chekform = True
                context = {'FormAddProduct': FormAddProduct,
                           'title': 'Добавить фото', 'PhotoOneProduct': FormAddPhotoProduct,
                           'chekform': chekform}
                return render(request, 'modersite/moder.html', context=context)

            context = {'FormAddProduct': FormAddProduct, 'title': '&&&',
                       'PhotoOneProduct': FormAddPhotoProduct,
                       'prod_id': ProductObj.id, 'chekform': chekform}
            return render(request, 'modersite/edit_product.html', context=context)
        else:
            FormAddProduct.add_error(None, 'form1 Ошибка добавления лота')
    FormAddProduct = AddProduct
    FormAddBrand = AddBrand
    FormAddProductType = AddProductType
    FormAddAgeCategory = AddAgeCategory
    FormAddSize = AddSize
    FormAddTextile=AddTextile
    ProdType = ProductType.objects.all()
    Brands = Brand.objects.all()
    AgeCategories = AgeCategory.objects.all()
    Sizes = Size.objects.all()
    Textiles = Textile.objects.all()
    context = {'FormAddProduct': FormAddProduct,
               'ProdAndPhoto': ShoweProduct,
               'FormAddBrand': FormAddBrand,
               'FormAddProductType': FormAddProductType,
               'FormAddAgeCategory': FormAddAgeCategory,
               'FormAddSize': FormAddSize,
               'FormAddTextile': FormAddTextile,
               'Brands': Brands,
               'ProdType': ProdType,
               'AgeCategories': AgeCategories,
               'Sizes': Sizes,
               'Textiles': Textiles,
               'ProductTypeList': ProductTypeList,
               'chekform': chekform}
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


def textile(request):
    if request.method == "POST":
        FormAddTextile = AddTextile(request.POST)
        if FormAddTextile.is_valid():
            SizeObj = FormAddTextile.save(commit=False)
            SizeObj.save()
            return redirect('moder')
        else:
            FormAddTextile.add_error(None, 'form1 Ошибка добавления ткани')
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
    elif table == 'Textile':
        Textile.objects.filter(id=id).delete()
    else:
        ErrMess = 'Не удалось определить модель или атрибут =( '
    return redirect('moder')


# Редактирование товара
def edit_product(request, prod_id):
    prod_edit = Product.objects.get(id=prod_id)
    if request.method == 'POST':
        # form = AddProduct(request.POST)
        form = AddProduct(request.POST, instance=prod_edit)
        if form.is_valid():
            # prod_edit.publication_status = moder_lot_status.objects.get(id=1)
            prod_edit.save()
            form.save()
            return redirect('moder')
    ProdDetails = Product.objects.get(id=prod_id)
    PhotoOneProduct = ProdDetails.images.all()
    FormAddPhotoProduct = AddPhotoProduct()
    context = {
        'prod_id': prod_id, 'PhotoOneProduct': PhotoOneProduct,
        'title': 'Редактирование товара', 'FormAddPhotoProduct': FormAddPhotoProduct,
        'prod_edit': prod_edit, 'FormAddProduct': AddProduct(instance=ProdDetails)}
    return render(request, 'modersite/edit_product.html',  context=context)


# Удаление одного фото
def delete_one_photo(request, prod_id, id_photo):
    if id_photo == 'no_data':
        del_photo = ''
    else:
        del_photo = PhotoProduct.objects.filter(id=id_photo, Product_link=prod_id)
    FormAddPhotoProduct = AddPhotoProduct()
    #del_photo = PhotoProduct.objects.filter(id=id_photo, Product_link=prod_id)
    del_photo.delete()
    ProductObj = Product.objects.get(id=prod_id)
    PhotoOneProduct = ProductObj.images.all()
    context = {
        'prod_id': prod_id, 'PhotoOneProduct': PhotoOneProduct,
        'title': 'Редактирование товара', 'prod_edit': ProductObj,
        'FormAddProduct': AddProduct(instance=ProductObj),
        'FormAddPhotoProduct': FormAddPhotoProduct}
    return render(request, 'modersite/edit_product.html', context=context)


# Удаление товара
def delete_product(request, prod_id):
    product_delete = Product.objects.filter(id=prod_id)
    photo_product_delete = PhotoProduct.objects.filter(Product_link=prod_id)
    product_delete.delete()
    if photo_product_delete:
        for ph in photo_product_delete:
            ph.product_photo.delete(save=True)
        photo_product_delete.delete()
    return redirect('moder')


def load_photo(request, ProductID):
    ProductLink = Product.objects.get(id=ProductID)
    if request.method == "POST":
        FormAddPhotoProduct = AddPhotoProduct(request.POST, request.FILES)
        if FormAddPhotoProduct.is_valid():
            try:
                loading = FormAddPhotoProduct.save(commit=False)
                loading.Product_link = ProductLink
                loading.save()
            except:
                FormAddPhotoProduct.add_error(None, 'form1 Ошибка добавления фото')
    else:
        FormAddPhotoProduct = AddPhotoProduct()
    PhotoOneProduct = PhotoProduct.objects.filter(Product_link=ProductID)
    context = {'FormAddPhotoProduct': FormAddPhotoProduct, 'title': 'Добавить фото',
               'PhotoOneProduct': PhotoOneProduct, 'prod_id': ProductID,
               'FormAddProduct': ProductLink}
    return render(request, 'modersite/edit_product.html', context=context)
