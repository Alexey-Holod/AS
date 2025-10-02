from django import template
from users.models import *
from home.OtherFunction import check_user_cart

register = template.Library()

@register.inclusion_tag('users/users_tags.html')
def get_categories(request, select = 'В_корзине'):
    # Получаем товары из корзины пользователя для того чтобы в дальнейшем показать количество товаров на разных этапах заказа.
    customer_basket = check_user_cart(request)
    cats = ['В_корзине', "Заказанные", "Куплено", 'Отмена']
    return {'cats':cats, 'select':select,
            # Заказано
            'quantity_of_goods': customer_basket['quantity_of_goods'],
            # Заказано
            'Sum_Ordered':customer_basket['Sum_Ordered'],
            # Куплинов
            'Sum_Purchased':customer_basket['Sum_Purchased'],
            # Отмененные
            'Sum_Cancelled':customer_basket['Sum_Cancelled']}
