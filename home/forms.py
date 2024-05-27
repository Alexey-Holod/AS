from django import forms


#Форма для поиска по диапозону цен в шаблоне shop.html
class PriceFormSearch(forms.Form):
    price_from = forms.CharField(widget=forms.TextInput(
                              attrs={'class': "price__filter--input__field border-0",
                                     'placeholder': '500'}), max_length=6)

    price_to = forms.CharField(widget=forms.TextInput(
                              attrs={'class': "price__filter--input__field border-0",
                                     'placeholder': '50000'}), max_length=6)

