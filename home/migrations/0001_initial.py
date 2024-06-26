# Generated by Django 5.0.3 on 2024-04-04 12:28

import django.db.models.deletion
import home.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age_range', models.CharField(max_length=1000, verbose_name='Возрастная категория')),
            ],
            options={
                'verbose_name': 'Возрастная категория',
                'verbose_name_plural': 'Возрастные категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=1000, verbose_name='Бренд')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender_name', models.CharField(max_length=1000, verbose_name='Гендер')),
            ],
            options={
                'verbose_name': 'Гендер',
                'verbose_name_plural': 'Гендеры',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age_range', models.CharField(max_length=1000, verbose_name='Тип_одежды')),
            ],
            options={
                'verbose_name': 'Тип одежды',
                'verbose_name_plural': 'Типы одежды',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_range', models.CharField(max_length=1000, verbose_name='Размер_одежды')),
            ],
            options={
                'verbose_name': 'Размер одежды',
                'verbose_name_plural': 'Размеры одежды',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_product', models.TextField(blank=True, max_length=1000, verbose_name='Название')),
                ('Product_price', models.CharField(max_length=20, verbose_name='Цена')),
                ('Product_code', models.CharField(max_length=1000, verbose_name='Артикул')),
                ('Posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('Product_age_category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='home.agecategory', verbose_name='Возростная категория')),
                ('Product_brand', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='home.brand', verbose_name='Бренд')),
                ('Product_gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.gender', verbose_name='Гендер')),
                ('Product_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='home.producttype', verbose_name='Тип одежды')),
                ('Product_size', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='home.size', verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товар',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PhotoProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_photo', models.ImageField(upload_to=home.models.user_directory_path, verbose_name='Фото')),
                ('Product_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Фото товара',
                'verbose_name_plural': 'Фотографии товара',
                'ordering': ['id'],
            },
        ),
    ]
