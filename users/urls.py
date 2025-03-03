from django.urls import path
from .views import *

urlpatterns = [
    path('/<int:user_id>', user_home, name='account'),
    path('user_cart/<str:flag>', user_cart, name='user_cart'),
    path('buy/<int:order_id>/<slug:flag>', buy, name='buy'),
    path('user_cart/prod_for_delete=<int:order_id>/<slug:flag>', user_cart_del, name='user_cart_del'),
    # path('user_cart_del/<int:user_id>/<int:order_id>', user_cart_del, name='user_cart_del'),
]
