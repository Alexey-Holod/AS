from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    Posted_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    Name_product = models.TextField(max_length=1000, blank=True, verbose_name='Название')
    Product_brand = models.ForeignKey('Brand', on_delete=models.PROTECT, blank=True, verbose_name='Бренд')
    Product_type = models.ForeignKey('ProductType', on_delete=models.PROTECT, blank=True, verbose_name='Тип одежды')
    Product_gender = models.ForeignKey('Gender', on_delete=models.PROTECT, blank=True, verbose_name='Гендер', null=True)
    Product_age_category = models.ForeignKey('AgeCategory', on_delete=models.PROTECT, blank=True, verbose_name='Возростная категория')
    Product_price = models.CharField(max_length=20, verbose_name='Цена')
    Product_code = models.CharField(max_length=1000, verbose_name='Артикул')
    Product_size = models.ManyToManyField('Size', verbose_name='Размер', related_name='sizes')
    def __str__(self):
        Product_ID = str(self.id)
        return Product_ID

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'
        ordering = ['id']


def user_directory_path(instance, filename):
    print("user_{0}/{1}".format(instance.Product_link.id, filename))
    return "photos/product/product_{0}/{1}".format(instance.Product_link.id, filename)


class PhotoProduct(models.Model):
    Product_link = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='images')
    product_photo = models.ImageField(upload_to=user_directory_path, verbose_name='Фото')

    def __str__(self):
        #car_link = int(self.car_link)
        return str(self.product_photo)

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фотографии товара'
        ordering = ['id']


class Brand(models.Model):
    brand_name = models.CharField(max_length=1000, verbose_name='Название Бренда')

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ['id']


class Gender(models.Model):
    gender_name = models.CharField(max_length=1000, verbose_name='Гендер')

    def __str__(self):
        return self.gender_name

    class Meta:
        verbose_name = 'Гендер'
        verbose_name_plural = 'Гендеры'
        ordering = ['id']


class AgeCategory(models.Model):
    Age_range = models.CharField(max_length=1000, verbose_name='Возрастная категория')

    def __str__(self):
        return self.Age_range

    class Meta:
        verbose_name = 'Возрастная категория'
        verbose_name_plural = 'Возрастные категории'
        ordering = ['id']


class ProductType(models.Model):
    Type = models.CharField(max_length=1000, verbose_name='Тип_одежды')

    def __str__(self):
        return self.Type

    class Meta:
        verbose_name = 'Тип одежды'
        verbose_name_plural = 'Типы одежды'
        ordering = ['id']


class Size(models.Model):
    size_range = models.CharField(max_length=1000, verbose_name='Размер_одежды')

    def __str__(self):
        return self.size_range

    class Meta:
        verbose_name = 'Размер одежды'
        verbose_name_plural = 'Размеры одежды'
        ordering = ['id']
