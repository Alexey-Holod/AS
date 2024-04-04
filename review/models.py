from django.db import models
from home.models import Product


class ProductReview(models.Model):
    ProductID = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, verbose_name='Товар')
    DataTime = models.DateTimeField(verbose_name='Название')
    Review = models.TextField(max_length=1000, blank=True, verbose_name='Отзыв')

    def __str__(self):
        ProductReview_ID = str(self.id)
        return ProductReview_ID

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['id']
