from django.db import models
from home.models import Product


class ProductDelivery(models.Model):
    ClientMAil = models.EmailField()
    ClientPhone = models.IntegerField(max_length=11,)
    ClientAddres = models.CharField(max_length=500,)
    ClientName = models.TextField(max_length=500,)
    ProductID = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, verbose_name='Товар')
    Name_product = models.ForeignKey('DeliveryStatus', on_delete=models.PROTECT, blank=True, verbose_name='Статус доставки')

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
        DeliveryStatus_ID = str(self.id)
        return DeliveryStatus_ID

    class Meta:
        verbose_name = 'Статус доставки'
        verbose_name_plural = 'Статусы доставки'
        ordering = ['id']
