from django import template
from users.models import *

register = template.Library()

@register.inclusion_tag('users/users_tags.html')
def get_categories(select = 'В_корзине'):
    cats = ['В_корзине', "Заказанные", "Куплено", 'Отмена']
    return {'cats':cats, 'select':select}