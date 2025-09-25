from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import *
from django.urls import path, include

# Сыылка по которо делался сброс пароля: https://fixmypc.ru/post/sozdanie-formy-vosstanovleniia-parolia-v-django/?ysclid=mfwhucge7x206868691#kak-realizuetsia-protsess-vosstanovleniia-parolia

urlpatterns = [
    path('in/', LoginView.as_view(template_name='auth_user_do/auth_in.html'), name='auth_user_do'),
    path('out/', LogoutView.as_view(), name='logout'),
    path('reg/', Reg.as_view(), name='registration'),
    path('reset_password/', PasswordResetView.as_view(template_name='auth_user_do/password_reset_form.html'),
         name ='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name='auth_user_do/password_reset_done.html'),
         name ='password_reset_done'),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='auth_user_do/password_reset_confirm.html'),
          name ='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='auth_user_do/password_reset_complete.html'),
         name ='password_reset_complete'),
]
