from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django import forms
from django.contrib.auth.models import User


class AuthRegUserForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Имя"}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Логин"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': "Пароль"}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': "Повторите пароль"}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': "Email"}))
    phone = forms.IntegerField(label='Телефон', widget=forms.NumberInput(attrs={'class': 'form-inputp', 'placeholder': "Телефон"}))

    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-authp'}),
            'username': forms.TextInput(attrs={'class': 'form-authp'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-authp'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-authp'}),
            'email': forms.EmailInput(attrs={'class': 'form-authp'}),
            'phone': forms.NumberInput(attrs={'class': 'form-authp'}),
        }
