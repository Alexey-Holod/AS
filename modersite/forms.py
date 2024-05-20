from django import forms
from home.models import *


#Форма для добавления товара
class AddProduct(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Product_brand'].empty_label = 'Не-выбрано'
        self.fields['Product_type'].empty_label = 'Не-выбрано'
        self.fields['Product_gender'].empty_label = 'Не-выбрано'
        self.fields['Product_age_category'].empty_label = 'Не-выбрано'

    Product_size = forms.ModelMultipleChoiceField(
        queryset=Size.objects.all(),
        widget=forms.SelectMultiple,
    )
    class Meta:
        model = Product
        fields = ['Name_product', 'Product_brand',
                  'Product_type', 'Product_gender',
                  'Product_age_category', 'Product_size',
                  'Product_price', 'Product_sale']
        widgets = {
            'Name_product': forms.TextInput(attrs={'class': 'datalot'}),
            'Product_brand': forms.Select(attrs={'class': 'datalot'}),
            'Product_type': forms.Select(attrs={'class': 'datalot'}),
            'Product_gender': forms.Select(attrs={'class': 'datalot'}),
            'Product_age_category': forms.Select(attrs={'class': 'datalot'}),
            'Product_price': forms.TextInput(attrs={'class': 'datalot', 'type': 'number', 'maxlength': '9'}),
            'Product_sale': forms.CheckboxInput(),
        }


#Форма для добавления бренда
class AddBrand(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name', ]
        widgets = {
            'brand_name': forms.TextInput(attrs={'class': 'datalot'}),
        }


#Форма для добавления
class AddProductType(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ['Type', 'TypeGender',]
        widgets = {
            'Type': forms.TextInput(attrs={'class': 'datalot'}),
            'TypeGender': forms.Select(attrs={'class': 'datalot'}),
        }


#Форма для добавления возростной категории
class AddAgeCategory(forms.ModelForm):
    class Meta:
        model = AgeCategory
        fields = ['Age_range', ]
        widgets = {
            'Age_range': forms.TextInput(attrs={'class': 'datalot'}),
        }


#Форма для добавления
class AddSize(forms.ModelForm):
    class Meta:
        model = Size
        fields = ['size_range', ]
        widgets = {
            'size_range': forms.TextInput(attrs={'class': 'datalot'}),
        }


#Форма для добавления фото
class AddPhotoProduct(forms.ModelForm):
    class Meta:
        model = PhotoProduct
        fields = ['product_photo', ]

        widgets = {
            'product_photo': forms.FileInput(),
        }
