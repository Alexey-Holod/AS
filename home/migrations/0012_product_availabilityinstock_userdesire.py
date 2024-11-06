# Generated by Django 5.0.6 on 2024-09-12 11:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_product_product_textile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='AvailabilityInStock',
            field=models.BooleanField(default=1, verbose_name='На складе'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserDesire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='home.product', verbose_name='Желаемое')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Желающий')),
            ],
        ),
    ]
