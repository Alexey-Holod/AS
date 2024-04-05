from django.contrib import admin
from .models import *

# class Product(admin.ModelAdmin):
#     list_display = ('id', 'Posted_by', 'Name_product', 'Product_brand')
#
#     list_display_links = ('id', 'Name_product')
#     search_fields = ('Name_product', 'Сar_model', 'Posted_by')
#     list_filter = ('Сar_years', 'Posted_by')

admin.site.register(Product)
admin.site.register(PhotoProduct)
admin.site.register(Brand)
admin.site.register(Gender)
admin.site.register(AgeCategory)
admin.site.register(ProductType)
admin.site.register(Size)
