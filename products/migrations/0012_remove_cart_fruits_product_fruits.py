# Generated by Django 4.1.4 on 2022-12-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_cart_fruits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='fruits',
        ),
        migrations.AddField(
            model_name='product',
            name='fruits',
            field=models.ManyToManyField(blank=True, to='products.cart'),
        ),
    ]
