# Generated by Django 5.0.6 on 2024-09-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_remove_productdelivery_clientmail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdelivery',
            name='date',
            field=models.DateField(blank=True, default=None),
        ),
    ]