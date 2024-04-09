from django import forms
from home.models import *


#Форма для добавления автомобиля
class AddProduct(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['Name_car_brand'].empty_label = 'Не-выбрано'
    #     self.fields['Сar_body_type'].empty_label = 'Не выбрано'
    #     self.fields['Car_state'].empty_label = 'Не выбрано'
    #     self.fields['transmission'].empty_label = 'Не выбрано'
    #     self.fields['Car_drive_unit'].empty_label = 'Не выбрано'
    #     self.fields['Car_city'].empty_label = 'Не выбрано'
    #     self.fields['Сar_owners'].empty_label = 'Не выбрано'
    #     self.fields['Сar_mileage'].empty_label = 'Не выбрано'
    #
    #     self.fields['car_front_axle'].empty_label = 'Не выбрано'
    #     self.fields['car_rear_axle'].empty_label = 'Не выбрано'
    #
    #     self.fields['Сar_engine'].empty_label = 'Не выбрано'

    class Meta:
        model = Product
        fields = ['Name_product', 'Product_brand',
                  'Product_type', 'Product_gender', 'Product_age_category',
                  'Product_size', 'Product_price']
        widgets = {
            'Name_product': forms.TextInput(attrs={'class': 'datalot'}),
            'Product_brand': forms.Select(attrs={'class': 'datalot'}),
            'Product_type': forms.Select(attrs={'class': 'datalot'}),
            'Product_gender': forms.Select(attrs={'class': 'datalot'}),
            'Product_age_category': forms.Select(attrs={'class': 'datalot'}),
            'Product_size': forms.Select(attrs={'class': 'datalot'}),
            'Product_price': forms.TextInput(attrs={'class': 'datalot', 'type': 'number', 'maxlength': '9'}),
        }


#Форма для добавления фото к машине
class AddPhotoProduct(forms.ModelForm):
    class Meta:
        model = PhotoProduct
        fields = ['product_photo', ]

        widgets = {
            'product_photo': forms.FileInput(attrs={'class': '#', }),
        }