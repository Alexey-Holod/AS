from django.db import models
from home.models import Product, Size
from django.contrib.auth.models import User


class ProductDelivery(models.Model):

    ClientPhone = models.IntegerField()
    ClientAddres = models.CharField(max_length=500,)
    ClientName = models.TextField(max_length=500,) # Имя заказчика
    Customer = models.ForeignKey(User, on_delete=models.CASCADE)
    Name_product = models.ForeignKey('DeliveryStatus', on_delete=models.PROTECT,
                                     blank=True, verbose_name='Статус доставки')
    ProductID = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, verbose_name='Товар')
    date = models.DateField(blank=True, default=None) # Дата заказа
    ProductSize = models.ForeignKey(Size, on_delete=models.PROTECT, blank=True, verbose_name='Размер')


    def __str__(self):
        ProductDelivery_ID = str(self.id)
        return ProductDelivery_ID

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'
        ordering = ['id']


class DeliveryStatus(models.Model):
    Status = models.TextField(max_length=500,)

    def __str__(self):
        DeliveryStatus_ID = str(self.Status)
        return DeliveryStatus_ID

    class Meta:
        verbose_name = 'Статус доставки'
        verbose_name_plural = 'Статусы доставки'
        ordering = ['id']
