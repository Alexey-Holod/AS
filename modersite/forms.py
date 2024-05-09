from django import forms
from home.models import *

HUITA0 = (('1', 'Huita1'), ('1', 'Huita1'), ('1', 'Huita1')),
#Форма для добавления автомобиля
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
                  'Product_price']
        widgets = {
            'Name_product': forms.TextInput(attrs={'class': 'datalot'}),
            'Product_brand': forms.Select(attrs={'class': 'datalot'}),
            'Product_type': forms.Select(attrs={'class': 'datalot'}),
            'Product_gender': forms.Select(attrs={'class': 'datalot'}),
            'Product_age_category': forms.Select(attrs={'class': 'datalot'}),
            'Product_price': forms.TextInput(attrs={'class': 'datalot', 'type': 'number', 'maxlength': '9'}),
        }


#Форма для добавления фото
class AddPhotoProduct(forms.ModelForm):
    class Meta:
        model = PhotoProduct
        fields = ['product_photo', ]

        widgets = {
            'product_photo': forms.FileInput(attrs={'class': '#', }),
        }