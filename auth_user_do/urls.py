from django.contrib.auth.views import LoginView, LogoutView
from .views import *
from django.urls import path

urlpatterns = [
    path('in/', LoginView.as_view(template_name='auth_user_do/auth_in.html'), name='auth_user_do'),
    path('out/', LogoutView.as_view(), name='logout'),
    path('reg/', Reg.as_view(), name='registration')
]
