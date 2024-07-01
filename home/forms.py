from django import forms
from .models import *


class PriceFormSearch(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Product_age_category'].empty_label = 'Не выбрано'

    price_from = forms.CharField(widget=forms.TextInput(
                              attrs={'class': "price__filter--input__field border-0",
                                     'placeholder': '500', 'value': '100'}), max_length=6)

    price_to = forms.CharField(widget=forms.TextInput(
                              attrs={'class': "price__filter--input__field border-0",
                                     'placeholder': '50000', 'value': '100000'}), max_length=6)

    class Meta:
        model = Product
        fields = ['Product_age_category']

        widgets = {
            'Product_age_category': forms.Select(attrs={'class': 'select_shop'}),
        }
